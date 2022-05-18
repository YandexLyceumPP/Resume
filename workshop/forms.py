from django import forms
from tinymce.widgets import TinyMCE

from workshop.models import Resume


class CreateResumeForm(forms.ModelForm):
    image = forms.ImageField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        fields = ('image', 'text')
        model = Resume
