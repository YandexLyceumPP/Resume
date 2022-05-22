from django import forms
from tinymce.widgets import TinyMCE

from workshop.models import Resume
from workshop.models import Contact


class ResumeForm(forms.ModelForm):
    # image = forms.ImageField()
    # text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    """skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all().only("skill"),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input me-1"})
    )"""
    
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
