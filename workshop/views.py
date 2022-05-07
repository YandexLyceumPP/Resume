from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def workshop(request):
    TEMPLATE = "workshop/create.html"
    return render(request, TEMPLATE)
