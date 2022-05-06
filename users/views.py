from django.contrib.auth import views, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import UserForm, UserLoginForm, UserRegistrationForm


def user_detail(request, user_name):
    TEMPLATE = "users/user_detail.html"
    context = {"user_name": user_name}
    return render(request, TEMPLATE, context)


def profile(request):
    TEMPLATE = "users/profile.html"
    return render(request, TEMPLATE)


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

    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_page(request):
    logout(request)
    return redirect("homepage")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect("users:profile")
    else:
        user_form = UserForm(instance=request.user)
    context = {
        "user_form": user_form,
    }
    return render(request, "users/profile.html", context=context)


class LoginView(views.LoginView):
    template_name = "users/login.html"


class LogoutView(views.LogoutView):
    template_name = "users/logout.html"


class PasswordChangeView(views.PasswordChangeView):
    template_name = "users/password_change.html"


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "users/password_change_done.html"


class PasswordResetView(views.PasswordResetView):
    template_name = "users/password_reset.html"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "users/reset.html"


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "users/reset_done.html"
