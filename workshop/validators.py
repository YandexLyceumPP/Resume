import re

from django.forms import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OrReValidator:
    def __init__(self, list_re, err_text="Переданное значение не "
                                         "соответствует не одному "
                                         "регулярному выражению"):
        self.list_re = list_re
        self.err_text = err_text

    def __call__(self, value):
        for i in self.list_re:
            if re.fullmatch(i, value):
                break
        else:
            raise ValidationError(self.err_text)
