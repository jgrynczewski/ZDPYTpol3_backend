from django.urls import path

from form_app3 import views

app_name = 'form3'

urlpatterns = [
    path('', views.index, name='index'),
    path('register-task/', views.register, name='register')
]