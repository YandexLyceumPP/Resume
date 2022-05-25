from django import forms
from django.contrib.auth import get_user_model

from core.forms import BaseForm
from users.models import Skill, Field, Profile

User = get_user_model()


class UserRegistrationForm(forms.ModelForm, BaseForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class ImageForm(forms.ModelForm, BaseForm):
    class Meta:
        model = Profile
        fields = ("image", )


class UserForm(forms.ModelForm, BaseForm):
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


class SearchUserForm(forms.Form, BaseForm):
    username = forms.CharField()
