from django.shortcuts import render


def about(request):
    TEMPLATE = "about/description.html"
    return render(request, TEMPLATE)
