from django.urls import path

from form_app import views

app_name = 'form'

urlpatterns = [
    path('', views.index, name='index'),
    path('register-task/', views.register, name='register'),
]
