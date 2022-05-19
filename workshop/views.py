from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView

from users.forms import FieldForm
from users.models import Field


@login_required
def workshop(request):
    TEMPLATE = "workshop/create.html"
    return render(request, TEMPLATE)


class FieldUpdate(LoginRequiredMixin, UpdateView):
    model = Field
    form_class = FieldForm
    template_name = "workshop/field/update.html"

    def get_queryset(self):
        return Field.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse("workshop:field_update", kwargs={"pk": self.object.id})
