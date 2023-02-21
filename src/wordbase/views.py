from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Word


def main(request):
    return render(request, 'wordbase/main.html')


def index(request):
    return HttpResponse('View: index')


def add_word(request):
    return HttpResponse('View: add_word')


def edit_word(request):
    return HttpResponse('View: edit_word')

def test(request):
    return HttpResponse('View: test')
