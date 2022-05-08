from django import forms

from tinymce.widgets import TinyMCE
from workshop.models import Icon
from users.models import Skill


class CreateSkillForm(forms.ModelForm):
    icon_choice = []
    icons = Icon.objects.all()
    cnt = 1
    for i in icons:
        icon_choice += [(i.id, i)]
        cnt += 1
    print(icon_choice)

    # skill = forms.CharField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    img = forms.ChoiceField(choices=icon_choice,  widget=forms.RadioSelect())

    class Meta:
        fields = ('skill', 'text', 'img')  # , 'img')
        model = Skill
