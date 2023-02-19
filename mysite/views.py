from django.shortcuts import render


def index(request):
    return render(request, 'mysite/MySiteTest1/index.html')
