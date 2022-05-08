from django import forms

# from workshop.models import Icon
from tinymce.widgets import TinyMCE

from users.models import Skill


class CreateSkillForm(forms.ModelForm):
    """icon_choice = ['sdc', 'sdc']
    icons = Icon.objects.all()
    cnt = 1
    for i in icons:
        icon_choice += [(cnt, i)]
        cnt += 1
    print(icon_choice)"""

    # skill = forms.CharField()
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    # img = forms.ChoiceField(choices=['324', '23432'])

    class Meta:
        fields = ('skill', 'text')  # , 'img')
        model = Skill
