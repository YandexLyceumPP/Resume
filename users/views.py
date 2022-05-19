from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

from users.models import Field, Profile
from users.forms import AddSkillForm, UserForm, UserRegistrationForm, FieldForm

from workshop.models import Resume

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


class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.get_or_create(user=request.user)[0]
        user_fields = Field.objects.filter(user=request.user).only("title", "value")

        user_form = UserForm(instance=request.user)
        skill_form = AddSkillForm(initial={"skills": profile.skills.all()})
        field_form = FieldForm()

        buttons = [
            {
                "class": "btn btn-danger",
                "url": reverse("users:logout"),
                "name": "Выйти",
            }
        ]

        context = {
            "forms": {
                "user_form": user_form,
                "skill_form": skill_form,
                "field_form": field_form,
            },
            "buttons": buttons,
            "user_fields": user_fields
        }
        return render(request, "users/profile.html", context=context)

    def post(self, request):
        user_form = UserForm(request.POST or None)
        skill_form = AddSkillForm(request.POST or None)
        field_form = FieldForm(request.POST or None)

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
