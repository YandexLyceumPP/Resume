from django.shortcuts import render


def workshop(request):
    TEMPLATE = "workshop/create.html"
    return render(request, TEMPLATE)
