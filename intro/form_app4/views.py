from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from form_app4.models import Message
from form_app4.forms import ContactForm2
from form_app4.forms import ContactForm3


#HTML Form
def contact1(request):

    if request.method == "POST":
        data = request.POST

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body')
        )

        # return redirect("form4:contact1")
        return HttpResponseRedirect(reverse("form4:contact1"))

    return render(request, "form_app4/contact1.html")


# Django form
def contact2(request):

    if request.method == "POST":

        form = ContactForm2(request.POST)  # bound form
        if form.is_valid():
            data = form.cleaned_data

            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body')
            )

        return redirect("form4:contact2")

    form = ContactForm2()  # unbound form
    return render(request, "form_app4/contact2.html", {"form": form})


# Model form
def contact3(request):

    if request.method == "POST":
        form = ContactForm3(request.POST)
        form.save()

        return HttpResponseRedirect(reverse("form_app4:contact3"))

    form = ContactForm3()
    return render(request, "form_app4/contact3.html", {"form": form})
