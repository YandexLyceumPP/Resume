from django.contrib.auth import views, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import View

from resume.settings.base import MEDIA_ROOT

from users.forms import SkillForm, UserForm, UserRegistrationForm, FieldForm
from users.models import Field, Profile

from workshop.forms import ContactForm
from workshop.models import Resume, Contact

User = get_user_model()


def user_detail(request, user_name):
    user = get_object_or_404(User, username=user_name)
    resumes = Resume.objects.filter(user=user)
    fields = Field.objects.filter(user=user)

    context = {
        "user": user,
        "resumes": resumes,
        "fields": fields
    }
    return render(request, "users/user_detail.html", context)


@method_decorator(login_required, name='get')
class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.get_or_create(user=request.user)[0]
        user_fields = Field.objects.filter(user=request.user).only("title", "value")
        user_contacts = Contact.objects.filter(user=request.user).only("contact")

        user_form = UserForm(instance=request.user)
        skill_form = SkillForm(initial={"skills": profile.skills.all()})
        field_form = FieldForm()
        contact_form = ContactForm()

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
            },
            "profile": profile,
            "buttons": buttons,
            "user_fields": user_fields,
            "user_contacts": user_contacts
        }
        return render(request, "users/profile.html", context=context)

    def post(self, request):
        user_form = UserForm(request.POST or None)
        skill_form = SkillForm(request.POST or None)
        field_form = FieldForm(request.POST or None)
        contact_form = ContactForm(request.POST or None)

        if skill_form.is_valid():
            profile = Profile.objects.get_or_create(user=request.user)[0]
            profile.skills.set(skill_form.cleaned_data["skills"])
            # profile.save(update_fields=["skills"])

        if user_form.is_valid():
            request.user.email = user_form.cleaned_data["email"]
            request.user.last_name = user_form.cleaned_data["last_name"]
            request.user.first_name = user_form.cleaned_data["first_name"]
            request.user.save(update_fields=["email", "last_name", "first_name"])

            profile = Profile.objects.get_or_create(user=request.user)[0]
            for filename, file in request.FILES.items():
                path = f'{MEDIA_ROOT}/upload/avatars/{request.FILES[filename].name}'
                with default_storage.open(path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                profile.image = f'upload/avatars/{request.FILES[filename].name}'
                profile.save(update_fields=["image"])

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
    return render(request, "users/signup.html", context)


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
    template_name = "users/login.html"
    extra_context = {"buttons": buttons}
