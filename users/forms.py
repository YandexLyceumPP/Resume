from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

from users.models import Skill


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
    # icons = Icon.objects.all()
    # icon_choice = [(i.id, i) for cnt, i in enumerate(icons, start=1)]

    # skill = forms.CharField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    # img = forms.ChoiceField(choices=icon_choice,  widget=forms.RadioSelect())

    class Meta:
        fields = ('skill', 'text')  # , 'img')
        model = Skill
