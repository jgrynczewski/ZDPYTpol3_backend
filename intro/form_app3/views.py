from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, 'form_app3/index.html')


def register(request):
    return render(request, 'form_app3/register.html')
