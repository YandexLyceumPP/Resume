from django.shortcuts import render, redirect
from workshop.models import Icon
from django import forms
from django.contrib.auth import views, authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import UserForm, UserLoginForm, UserRegistrationForm


class CreateSkillForm(forms.Form):
    icon_choice = []
    icons = Icon.objects.all()
    cnt = 1
    for i in icons:
        icon_choice  += [(cnt, i)]
        cnt += 1
    print(icon_choice)
    skill = forms.CharField()
    text = forms.CharField()
    img = forms.ChoiceField(choices=icon_choice,  widget=forms.RadioSelect())

def user_detail(request, user_name):
    TEMPLATE = "users/user_detail.html"
    context = {"user_name": user_name}
    return render(request, TEMPLATE, context)





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

def profile(request):
    TEMPLATE = "users/profile.html"
    return render(request, TEMPLATE)


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        form = CreateSkillForm(request.POST or None)
        if user_form.is_valid():
            user_form.save()
            return redirect("users:profile")
    else:
        user_form = UserForm(instance=request.user)
        form = CreateSkillForm(request.POST or None)
    context = {
        "user_form": user_form,
        "form": form,
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
