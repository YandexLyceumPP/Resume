from django.http import HttpResponse
# from django.shortcuts import render


def user_detail(request, user_name):
    return HttpResponse(f'Подробный просмотр пользователя {user_name}')


def profile(request):
    return HttpResponse('Просмотр страницы авторизованного пользователя')
