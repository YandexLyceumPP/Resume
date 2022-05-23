from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView, DetailView

from users.forms import FieldForm
from users.models import Field

from workshop.forms import CreateResumeForm, ResumeForm
from workshop.models import Contact, Resume, Block, Text, File


# Resume

@login_required
def resume_create(request):
    if request.method == "POST":
        form = CreateResumeForm(request.POST or None, request.FILES)
        if form.is_valid():
            resume = Resume(
                user=request.user,
                image=form.cleaned_data["image"],
                text=form.cleaned_data["text"],
            )
            resume.save()
            return redirect("users:profile")
    else:
        form = CreateResumeForm()

    context = {
        "form": form,
    }
    return render(request, "workshop/resume/create.html", context=context)


@login_required
def resume_update(request, pk):
    resume = get_object_or_404(Resume, id=pk, user=request.user)
    if request.method == "POST":
        form = ResumeForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            resume.image = form.cleaned_data["image"]
            resume.text = form.cleaned_data["text"]
            resume.save(update_fields=["image", "text"])
            resume.contacts.set(form.cleaned_data["contacts"])
            resume.tags.set(form.cleaned_data["tags"])
            return redirect("users:profile")
    else:
        form = ResumeForm(request.user, instance=resume)

    context = {
        "form": form,
    }
    return render(request, "workshop/resume/update.html", context=context)


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


# Resume

class ResumeDetailView(DetailView):
    model = Resume
    template_name = "workshop/resume/detail.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        blocks = Block.objects.filter(resume=self.object.id)
        context['blocks'] = blocks
        for i in range(len(blocks)):
            blocks[i].files = File.objects.filter(block=blocks[i].id)
        return context