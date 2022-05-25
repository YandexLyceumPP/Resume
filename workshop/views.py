from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import UpdateView, DeleteView, DetailView

from users.forms import FieldForm
from users.models import Field

from workshop.forms import CreateResumeForm, ResumeForm, BaseBlockForm, FileBlockForm
from workshop.models import Contact, Resume, Block, File, Text, Tag


# Resume

class ResumeDetailView(DetailView):
    model = Resume
    template_name = "workshop/resume/detail.html"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get("pk")

        try:
            obj = queryset.only("date_edit", "image", "text", "user_id").prefetch_related(
                Prefetch("tags", queryset=Tag.objects.only("name"))
            ).prefetch_related(
                Prefetch("contacts", queryset=Contact.objects.only("contact"))
            ).get(id=pk)
        except queryset.model.DoesNotExist:  # Если объект не найден
            raise Http404("Не удалось найти нужное резюме")

        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blocks = Block.objects.filter(resume=self.object.id).only("order", "title", "date_edit")
        for i in range(len(blocks)):
            blocks[i].files = File.objects.filter(block=blocks[i].id).only("file")

        context["blocks"] = blocks.prefetch_related("text")
        return context


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
    template_name = "core/delete.html"
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delete_message"] = "резюме"
        buttons = [
            {
                "class": "btn btn-primary",
                "url": reverse_lazy("workshop:resume_detail", args=[self.object.id]),
                "name": "Назад",
            }
        ]
        context["buttons"] = buttons
        return context


# Field

class FieldUpdateView(LoginRequiredMixin, UpdateView):
    model = Field
    form_class = FieldForm
    template_name = "workshop/field/update.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("workshop:field_update", kwargs={"pk": self.object.id})


class FieldDeleteView(LoginRequiredMixin, DeleteView):
    model = Field
    template_name = "core/delete.html"
    success_url = reverse_lazy("users:profile")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delete_message"] = f"факт '{self.object.title}'"
        buttons = [
            {
                "class": "btn btn-primary",
                "url": reverse_lazy("users:profile"),
                "name": "Назад",
            }
        ]
        context["buttons"] = buttons
        return context


# Contact

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "core/delete.html"
    success_url = reverse_lazy("users:profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["delete_message"] = f"контакт '{self.object.contact}'"
        buttons = [
            {
                "class": "btn btn-primary",
                "url": reverse_lazy("users:profile"),
                "name": "Назад",
            }
        ]
        context["buttons"] = buttons
        return context

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# Block

def block_changing_order(request, pk, direction):
    block = Block.objects.get(pk=pk)
    if block.resume.user == request.user:
        match direction:
            case "up":
                block.up()
            case "down":
                block.down()

    return redirect("workshop:resume_detail", pk=block.resume.id)


class BlockDeleteView(LoginRequiredMixin, DeleteView):
    model = Block
    template_name = "workshop/block/delete.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("workshop:resume_detail", kwargs={"pk": self.object.resume.id})


class BlockCreateView(LoginRequiredMixin, View):
    def get(self, request, resume_id):
        form = BaseBlockForm()

        context = {"form": form}
        return render(request, "workshop/block/create.html", context=context)

    def post(self, request, resume_id):
        resume = get_object_or_404(Resume, user=request.user, id=resume_id)

        form = BaseBlockForm(request.POST or None)
        if form.is_valid():
            block = Block(
                resume=resume,
                title=form.cleaned_data["title"]
            )
            block.save()

            if form.cleaned_data["text"]:
                Text(
                    block=block,
                    text=form.cleaned_data["text"]
                ).save()

        return redirect("workshop:resume_detail", pk=resume_id)


class BlockUpdateView(LoginRequiredMixin, View):
    def get(self, request, resume_id, pk):
        get_object_or_404(Resume, user=request.user, id=resume_id)  # Ну эту строку я переделаю)
        block = get_object_or_404(Block, pk=pk)
        text = Text.objects.filter(block=block)
        files = File.objects.filter(block=block)

        base_form = BaseBlockForm(
            initial={
                "title": block.title,
                "text": text.first().text if text else ""
            }
        )
        file_form = FileBlockForm()

        context = {
            "forms": {
                "base": base_form,
                "file": file_form
            },
            "files": files,
            "block_id": block.id
        }
        return render(request, "workshop/block/update.html", context=context)

    def post(self, request, resume_id, pk):
        resume = get_object_or_404(Resume, user=request.user, id=resume_id)
        block = get_object_or_404(Block, resume=resume, id=pk)

        base_form = BaseBlockForm(request.POST or None)
        file_form = FileBlockForm(request.POST or None, request.FILES or None)

        if base_form.is_valid():
            block.title = base_form.cleaned_data["title"]
            block.save(update_fields=("title", ))

            if base_form.cleaned_data["text"]:
                text = Text.objects.get_or_create(block=block)[0]
                text.text = base_form.cleaned_data["text"]
                text.save(update_fields=("text", ))
            else:
                text = Text.objects.filter(block=block)
                if text:
                    text.delete()

        if file_form.is_valid():
            File(
                block=block,
                file=file_form.cleaned_data["file"]
            ).save()

        return redirect("workshop:block_update", resume_id=resume_id, pk=pk)


# File
class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = File
    template_name = "workshop/file/delete.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_success_url(self):
        block = self.object.block
        return reverse_lazy("workshop:block_update", kwargs={"resume_id": block.resume.id, "pk": block.id})
