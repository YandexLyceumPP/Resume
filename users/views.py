from django.shortcuts import render

from users.forms import CreateSkillForm


def user_detail(request, user_name):
    TEMPLATE = "users/user_detail.html"

    context = {"user_name": user_name}
    return render(request, TEMPLATE, context)


def profile(request):
    TEMPLATE = "users/profile.html"
    form = CreateSkillForm(request.POST or None)
    context = {"form": form}
    return render(request, TEMPLATE, context=context)
