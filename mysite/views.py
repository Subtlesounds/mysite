from django.shortcuts import render
from settings import BASE_DIR


def index(request):
    return render(request, BASE_DIR/'MySiteTest1/index.html')
