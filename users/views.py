from django.shortcuts import render


def user_detail(request, user_name):
    TEMPLATE = "users/user_detail.html"
    context = {
        "user_name": user_name
    }
    return render(request, TEMPLATE, context)


def profile(request):
    TEMPLATE = "users/profile.html"
    return render(request, TEMPLATE)
