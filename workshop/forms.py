from django import forms

from workshop.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ("contact", )
        model = Contact
