from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('Essa pagina esta vindo direto do app NusediagPredictor')


def csand(request):
    return HttpResponse('Aqui será a pagina de previsao e está vindo de NurseDiagPredictor')