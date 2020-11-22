from django.shortcuts import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<!DOCTYPE html><html><head><title>ABC</title></head><body><h2>Hello, world!</h2></body></html>")


def hello2(request):
    return render(request, 'templates/hello.html')