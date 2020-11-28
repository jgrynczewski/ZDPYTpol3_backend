from django.shortcuts import render


# Create your views here.
def first(request):
    return render(request, 'inheritance/first_view.html')


def second(request):
    return render(request, 'inheritance/second_view.html')