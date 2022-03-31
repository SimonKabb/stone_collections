from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'stones/index.html')


def stones():
    return HttpResponse('Камни')


def stone_detail(request, pk):
    return HttpResponse(f'Камень номер {pk}')
