from django.shortcuts import render


def home(request):
    TEMPLATE = "homepage/homepage.html"
    return render(request, TEMPLATE)


def error_404(request, exception):
    TEMPLATE = "errors/error_404.html"
    return render(request, TEMPLATE, status=404)
