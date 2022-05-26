from django import forms
from tinymce.widgets import TinyMCE

from core.forms import BaseForm
from workshop.models import Contact, Resume


class ResumeForm(forms.ModelForm, BaseForm):
    def __init__(self, user=None, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        for field in ("tags", "contacts"):
            self.fields[field].widget = forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input me-1"}
            )

        if user:
            self.fields["contacts"].queryset = Contact.objects.filter(
                user=user)

    class Meta:
        fields = ("image", "tags", "contacts", "show", "text")
        model = Resume


class CreateResumeForm(forms.ModelForm, BaseForm):
    class Meta:
        fields = ("image", "text")
        model = Resume


class ContactForm(forms.ModelForm, BaseForm):
    class Meta:
        fields = ("contact",)
        model = Contact


class BaseBlockForm(forms.Form, BaseForm):
    title = forms.CharField(label="Название", max_length=200)
    text = forms.CharField(
        label="Содержание",
        widget=TinyMCE(attrs={"cols": 80, "rows": 10}),
        required=False,
    )


class FileBlockForm(forms.Form, BaseForm):
    file = forms.FileField(label="Файл")
