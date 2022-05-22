from django import forms
from tinymce.widgets import TinyMCE

from workshop.models import Resume
from workshop.models import Contact


class ResumeForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

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
