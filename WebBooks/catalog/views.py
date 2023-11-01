from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<h1>Главная страница сайта "Мир книг"</h1>')
