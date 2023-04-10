from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    return HttpResponse('Добро пожаловать в наш магазин!')