from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView

from users.forms import FieldForm
from users.models import Field
from workshop.models import Contact


@login_required
def workshop(request):
    TEMPLATE = "workshop/create.html"
    return render(request, TEMPLATE)


class FieldUpdateView(LoginRequiredMixin, UpdateView):
    model = Field
    form_class = FieldForm
    template_name = "workshop/field/update.html"

    def get_queryset(self):
        return Field.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("workshop:field_update", kwargs={"pk": self.object.id})


class FieldDeleteView(LoginRequiredMixin, DeleteView):
    model = Field
    template_name = "workshop/field/delete.html"

    success_url = reverse_lazy("users:profile")


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "workshop/contact/delete.html"

    success_url = reverse_lazy("users:profile")
