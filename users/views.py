from django.contrib.auth import views, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView

from resume.settings.base import MEDIA_ROOT

from users.forms import SkillForm, UserForm, UserRegistrationForm, FieldForm, SearchUserForm, ImageForm
from users.models import Field, Profile, Skill

from workshop.forms import ContactForm
from workshop.models import Resume, Contact, Tag

User = get_user_model()


class SearchUserView(View):
    def get(self, request, username):
        form = SearchUserForm(initial={"username": username})

        context = {"form": form}
        return render(request, "users/search_user.html", context=context)

    def post(self, request, username):
        form = SearchUserForm(request.POST or None)

        if form.is_valid():
            return redirect("users:detail", username=form.cleaned_data["username"])

        return redirect("users:search", username=form.cleaned_data["username"])


class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

        return redirect("users:search", username=self.kwargs.get("username"))

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        username = self.kwargs.get("username")

        try:
            obj = queryset.filter(username=username).prefetch_related(
                Prefetch(
                    "profile",
                    queryset=Profile.objects.prefetch_related(
                        Prefetch("skills", queryset=Skill.objects.only("skill"))
                    )
                )
            ).get()
        except queryset.model.DoesNotExist:  # Если объект не найден
            # raise Http404("Не удалось найти нужного пользователя")
            return

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resumes"] = Resume.objects.get_show().filter(
            user=self.object).only("image", "date_edit", "text").prefetch_related(
            Prefetch("tags", queryset=Tag.objects.only("name")))
        context["fields"] = Field.objects.get_show().filter(user=self.object).only("title", "value")
        return context


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        profile = Profile.objects.prefetch_related(
            Prefetch("skills", queryset=Skill.objects.only("skill"))
        ).get_or_create(user=request.user)[0]
        resumes = Resume.objects.filter(user=request.user).only("image", "date_edit", "text").prefetch_related(
            Prefetch("tags", queryset=Tag.objects.only("name"))
        )
        user_fields = Field.objects.filter(user=request.user).only("title", "value")
        user_contacts = Contact.objects.filter(user=request.user).only("contact")

        user_form = UserForm(instance=request.user)
        skill_form = SkillForm(initial={"skills": profile.skills.all()})
        field_form = FieldForm()
        contact_form = ContactForm()
        image_form = ImageForm()

        buttons = [
            {
                "class": "btn btn-danger",
                "url": reverse_lazy("users:logout"),
                "name": "Выйти",
            }
        ]

        context = {
            "forms": {
                "user": user_form,
                "skill": skill_form,
                "field": field_form,
                "contact": contact_form,
                "image": image_form,
            },
            "profile": profile,
            "buttons": buttons,
            "user_fields": user_fields,
            "user_contacts": user_contacts,
            "resumes": resumes
        }
        return render(request, "users/profile.html", context=context)

    def post(self, request):
        user_form = UserForm(request.POST or None)
        skill_form = SkillForm(request.POST or None)
        field_form = FieldForm(request.POST or None)
        contact_form = ContactForm(request.POST or None)
        image_form = ImageForm(request.POST or None, request.FILES)

        if skill_form.is_valid():
            profile = Profile.objects.get_or_create(user=request.user)[0]
            profile.skills.set(skill_form.cleaned_data["skills"])
            # profile.save(update_fields=["skills"])

        if user_form.is_valid():
            request.user.email = user_form.cleaned_data["email"]
            request.user.last_name = user_form.cleaned_data["last_name"]
            request.user.first_name = user_form.cleaned_data["first_name"]
            request.user.save(update_fields=["email", "last_name", "first_name"])

        if field_form.is_valid():
            Field(
                user=request.user,
                title=field_form.cleaned_data["title"],
                value=field_form.cleaned_data["value"]
            ).save()

        if contact_form.is_valid():
            Contact(
                user=request.user,
                contact=contact_form.cleaned_data["contact"]
            ).save()

        if image_form.is_valid():
            profile = Profile.objects.get_or_create(user=request.user)[0]
            profile.image = image_form.cleaned_data["image"]
            profile.save(update_fields=["image"])

        return redirect("users:profile")


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return redirect("users:login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "users/authorization/signup.html", context)


class LoginView(views.LoginView):
    buttons = [
        {
            "class": "btn btn-primary",
            "url": reverse_lazy("users:signup"),
            "name": "Регистрация",
        },
        {
            "class": "btn btn-danger",
            "url": reverse_lazy("users:password_reset"),
            "name": "Забыл пароль",
        }
    ]

    authentication_form = AuthenticationForm
    redirect_authenticated_user = True
    template_name = "users/authorization/login.html"
    extra_context = {"buttons": buttons}


# Skill

class SkillDetailView(DetailView):
    model = Skill
    template_name = "users/skill_detail.html"
