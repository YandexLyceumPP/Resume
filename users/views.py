from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views, authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views import View
from users.forms import UserForm, UserLoginForm, UserRegistrationForm, AddSkillForm
from users.models import Field, Profile
from workshop.models import Resume
from django.urls import reverse, reverse_lazy
from users.forms import UserForm, UserLoginForm, UserRegistrationForm

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


def login_page(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is None:
                form.add_error(None, "Пользователь не найден")
            elif user.is_active:
                login(request, user)
                return redirect("users:profile")
            else:
                form.add_error(None, "Аккаунт не активен")
    else:
        form = UserLoginForm()

    buttons = [
        {
            'class': 'btn btn-primary',
            'url': reverse('users:signup'),
            'name': 'Регистрация',
        },
        {
            'class': 'btn btn-danger',
            'url': reverse('users:password_reset'),
            'name': 'Забыл пароль',
        }
    ]

    context = {
        "form": form,
        "buttons": buttons,
    }

    return render(request, "users/login.html", context)


def logout_page(request):
    logout(request)
    return redirect("homepage")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST or None, instance=request.user)
        # skill_form = AddSkillForm(request.POST or None)
        if user_form.is_valid():
            user_form.save()
            return redirect("users:profile")
    else:
        user_form = UserForm(instance=request.user)
        skill_form = AddSkillForm(instance=request.user)
        # skill_form = AddSkillForm(request.POST or None)
    buttons = [
        {
            'class': 'btn btn-danger',
            'url': reverse('users:logout'),
            'name': 'Выйти',
        }
    ]
    context = {
        "user_form": user_form,
        # "skill_form": skill_form,
        "buttons": buttons,
    }
    return render(request, "users/profile.html", context=context)


class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.get_or_create(user=request.user)[0]

        user_form = UserForm(instance=request.user)
        skill_form = AddSkillForm(initial={"skills": profile.skills.all()})

        context = {
            "user_form": user_form,
            "skill_form": skill_form,
        }
        return render(request, "users/profile.html", context=context)

    def post(self, request):
        user_form = UserForm(request.POST or None)
        skill_form = AddSkillForm(request.POST or None)

        if skill_form.is_valid():
            profile = Profile.objects.get_or_create(user=request.user)[0]
            profile.skills.set(skill_form.cleaned_data["skills"])
            # profile.save(update_fields=["skills"])

        if user_form.is_valid():
            request.user.email = user_form.cleaned_data["email"]
            request.user.last_name = user_form.cleaned_data["last_name"]
            request.user.first_name = user_form.cleaned_data["first_name"]
            request.user.save(update_fields=["email", "last_name", "first_name"])

        return redirect("users:profile")


def settings(request):
    TEMPLATE = "users/settings.html"
    return render(request, TEMPLATE)


@login_required
def settings(request):
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:settings")
    else:
        form = UserForm(instance=request.user)
    buttons = [
        {
            'class': 'btn btn-danger',
            'url': reverse('users:logout'),
            'name': 'Выйти',
        }
    ]
    context = {
        "form": form,
        "buttons": buttons,
    }
    return render(request, "users/settings.html", context=context)


class LogoutView(views.LogoutView):
    template_name = "users/logout.html"


class PasswordChangeView(views.PasswordChangeView):
    template_name = "users/password_change.html"


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "users/password_change_done.html"


class PasswordResetView(views.PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "users/reset.html"


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "users/reset_done.html"
