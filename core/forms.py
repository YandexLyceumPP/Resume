from django.forms import forms


class BaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-check-input" if visible.name in ("show",
                                                                                         "skills") else "form-control"
