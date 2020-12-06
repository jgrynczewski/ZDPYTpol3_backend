from django import forms

from form_app4 import models

class ContactForm2(forms.Form):
    CHOICES = [
        ("", "------------------------"),
        ("question", "Pytanie"),
        ("other", "Inne"),
    ]
    name = forms.CharField(label="Imię", required=False)
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(label="Kategoria", choices=CHOICES)
    subject = forms.CharField(label="Tytuł")
    body = forms.CharField(label="Treść", widget=forms.Textarea)


class ContactForm3(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = "__all__"
