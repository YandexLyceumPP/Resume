from django import forms
from django.shortcuts import render

from workshop.models import Icon


class CreateSkillForm(forms.Form):
    icon_choice = []
    '''icons = Icon.objects.all()
    cnt = 1
    for i in icons:
        icon_choice += [(cnt, i)]
        cnt += 1'''

    print(icon_choice)
    skill = forms.CharField()
    text = forms.CharField()
    img = forms.ChoiceField(choices=icon_choice,  widget=forms.RadioSelect())


def user_detail(request, user_name):
    TEMPLATE = "users/user_detail.html"

    context = {"user_name": user_name}
    return render(request, TEMPLATE, context)


def profile(request):
    TEMPLATE = "users/profile.html"
    form = CreateSkillForm(request.POST or None)

    context = {"form": form}
    return render(request, TEMPLATE, context=context)
