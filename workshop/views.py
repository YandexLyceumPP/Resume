from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, DetailView

from users.forms import FieldForm
from users.models import Field

from workshop.forms import CreateResumeForm
from workshop.models import Contact, Resume


@login_required
def workshop(request):
    if request.method == "POST":
        form = CreateResumeForm(request.POST or None, request.FILES)
        if form.is_valid():
            resume = Resume(
                user=request.user,
                image=form.cleaned_data["image"],
                text=form.cleaned_data["text"],
                date_edit=form.cleaned_data["date_edit"],
            )
            resume.save()
            resume.contacts.set(form.cleaned_data["contacts"])
            resume.tags.set(form.cleaned_data["tags"])
            return redirect("users:profile")
    else:
        form = CreateResumeForm()
    context = {
        "form": form,
    }
    return render(request, "workshop/create.html", context=context)


# Field

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


# Contact

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "workshop/contact/delete.html"

    success_url = reverse_lazy("users:profile")


# Resume

class ResumeDetailView(DetailView):
    model = Resume
    template_name = "workshop/resume/detail.html"
