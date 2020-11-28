import datetime

from markupsafe import escape
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Witaj, świecie!")


def hi(request):
    return render(request, "next_app/hi.html")


def parameters(request, param):
    sanitize_param = escape(param)
    return HttpResponse(f"Hello {sanitize_param}")


def templates(request):
    n = "Jan"
    return render(request, "next_app/4.html", {'name': n})


def templates2(request, param):
    return render(request, "next_app/5.html", {"param": param})


def is_it_monday(request):
    now = datetime.datetime.now()
    is_monday = True if now.weekday() == 0 else False

    return render(request, "next_app/6.html", {"is_monday": is_monday})

def fruits(request):
    fruits = ['apple', 'banana', 'orange', 'watermelon']

    return render(
        request,
        'next_app/7.html',
        {"fruits": fruits}
    )
