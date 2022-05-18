from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from workshop.forms import CreateResumeForm


@login_required
def workshop(request):
    if request.method == "POST":
        form = CreateResumeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = CreateResumeForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, "workshop/create.html", context=context)
