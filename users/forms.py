from django import forms
from django.contrib.auth.models import User

from tinymce.widgets import TinyMCE
from workshop.models import Icon
from users.models import Skill
from .models import Profile


class BaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class UserLoginForm(forms.Form, BaseForm):
    username = forms.CharField(label="Имя пользователя / Email")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm, BaseForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]


class UserForm(forms.ModelForm, BaseForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")



class CreateSkillForm(forms.ModelForm):
    icon_choice = []
    icons = Icon.objects.all()
    cnt = 1
    for i in icons:
        icon_choice += [(i.id, i)]
        cnt += 1
    print(icon_choice)

    # skill = forms.CharField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    img = forms.ChoiceField(choices=icon_choice,  widget=forms.RadioSelect())

    class Meta:
        fields = ('skill', 'text', 'img')  # , 'img')
        model = Skill
