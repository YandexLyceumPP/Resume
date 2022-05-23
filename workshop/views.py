from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView

from users.forms import FieldForm
from users.models import Field

from workshop.forms import CreateResumeForm, ResumeForm
from workshop.models import Contact, Resume


# Resume

class ResumeDetailView(DetailView):
    model = Resume
    template_name = "workshop/resume/detail.html"


class ResumeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateResumeForm()

        context = {"form": form}
        return render(request, "workshop/resume/create.html", context=context)

    def post(self, request):
        form = CreateResumeForm(request.POST or None, request.FILES)
        if form.is_valid():
            resume = Resume(
                user=request.user,
                image=form.cleaned_data["image"],
                text=form.cleaned_data["text"],
            )
            resume.save()

            return redirect("workshop:resume_detail", pk=resume.id)

        return redirect("workshop:resume_create")


class ResumeUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        resume = get_object_or_404(Resume, id=pk, user=request.user)
        form = ResumeForm(request.user, instance=resume)

        context = {"form": form}
        return render(request, "workshop/resume/update.html", context=context)

    def post(self, request, pk):
        resume = get_object_or_404(Resume, id=pk, user=request.user)

        form = ResumeForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data["image"] is False:
                resume.image = None
            elif form.cleaned_data["image"]:
                resume.image = form.cleaned_data["image"]

            resume.text = form.cleaned_data["text"]
            resume.save(update_fields=["image", "text"])

            resume.contacts.set(form.cleaned_data["contacts"])
            resume.tags.set(form.cleaned_data["tags"])

        return redirect("workshop:resume_update", pk=pk)


class ResumeDeleteView(LoginRequiredMixin, DeleteView):
    model = Resume
    template_name = "workshop/resume/delete.html"

    success_url = reverse_lazy("users:profile")


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
