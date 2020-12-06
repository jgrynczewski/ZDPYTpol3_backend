from django.urls import path

from class_app import views

app_name = 'class'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),
    path('person/<int:id>', views.person_detail, name='person_detail'),
    path('person2/<int:id>', views.PersonView.as_view(), name='person_detail2'),
    path('person3/<int:pk>', views.PersonDetailView.as_view(), name='person_detail3'),
]