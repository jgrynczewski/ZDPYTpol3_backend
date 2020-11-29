from django.urls import path

from form_app2 import views

app_name = 'form2'

urlpatterns = [
    path('', views.index, name='index'),
    path('register-task/', views.register, name='register')
]