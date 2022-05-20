from django import forms
from django.contrib.auth.models import User

from users.models import Skill, Field


class BaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


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
    image = forms.ImageField(required=False)
    field_order = ("image", "first_name", "last_name", "email")


    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class SkillForm(forms.ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().only("skill"),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input me-1"})
    )

    class Meta:
        fields = ("skills", )
        model = Skill


class FieldForm(forms.ModelForm):
    class Meta:
        fields = ("title", "show", "value")
        model = Field
