from django import forms
from django.contrib.auth.models import User

from core.forms import BaseForm
from users.models import Skill, Field


class UserRegistrationForm(forms.ModelForm, BaseForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserForm(forms.ModelForm, BaseForm):
    image = forms.ImageField(required=False)
    field_order = ("image", "first_name", "last_name", "email")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class SkillForm(forms.ModelForm, BaseForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().only("skill"),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input me-1"})
    )

    class Meta:
        fields = ("skills", )
        model = Skill


class FieldForm(forms.ModelForm, BaseForm):
    class Meta:
        fields = ("title", "show", "value")
        model = Field
