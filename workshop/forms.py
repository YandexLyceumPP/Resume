from audioop import reverse

from django import forms
from tinymce.widgets import TinyMCE

from workshop.models import Resume, Contact, Block


class ResumeForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        for field in ("tags", "contacts"):
            self.fields[field].widget = forms.CheckboxSelectMultiple(attrs={"class": "form-check-input me-1"})

        if user:
            self.fields["contacts"].queryset = Contact.objects.filter(user=user)

    class Meta:
        fields = ("image", "tags", "contacts", "text")
        model = Resume


class CreateResumeForm(forms.ModelForm):
    class Meta:
        fields = ("image", "text")
        model = Resume


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ("contact", )
        model = Contact


class BaseBlockForm(forms.Form):
    title = forms.CharField(label="Название", max_length=200)
    text = forms.CharField(label="Содержание", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)


class FileBlockForm(forms.Form):
    file = forms.FileField(label="Файл")
