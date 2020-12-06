from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django import views

from class_app.models import Person

# Function-based views
def hello(request):
    return HttpResponse("Hello, world!")


# Class-based view
class HelloView(views.View):
    def get(self, request):
        return HttpResponse("Hello, word!")


# Function-based view
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)
    return render(request, 'class_app/person.html', {"person": p})


# Class-based view
class PersonView(views.View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)
        return render(request, 'class_app/person.html', {"person": p})


# Generic views
class PersonDetailView(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context
