from django.shortcuts import render


def home(request):
    TEMPLATE = "homepage/homepage.html"
    return render(request, TEMPLATE)
