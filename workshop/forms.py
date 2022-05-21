from django import forms
from tinymce.widgets import TinyMCE

from workshop.models import Resume
from workshop.models import Contact


class CreateResumeForm(forms.ModelForm):
    image = forms.ImageField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        fields = ("image", "text", "contacts", "tags", "date_edit")
        model = Resume


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ("contact", )
        model = Contact
