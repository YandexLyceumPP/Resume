from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from users.forms import CreateSkillForm
from users.forms import UserForm, UserRegistrationForm


def user_detail(request, user_name):
    TEMPLATE = "users/user_detail.html"
    context = {"user_name": user_name}
    return render(request, TEMPLATE, context)


@login_required
def profile(request):
    if request.method == "POST":
        form = CreateSkillForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = CreateSkillForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, "users/profile.html", context=context)


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
            'url': reverse_lazy('users:logout'),
            'name': 'Выйти',
        }
    ]
    context = {
        "form": form,
        "buttons": buttons,
    }
    return render(request, "users/settings.html", context=context)


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


class LogoutView(views.LogoutView):
    next_page = reverse_lazy("users:login")
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
