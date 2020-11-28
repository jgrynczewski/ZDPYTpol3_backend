from django.urls import path

from next_app import views

urlpatterns = [
    path('1/', views.hello),
    path('2/', views.hi),
    path('3/<str:param>/', views.parameters),
    path('4/', views.templates),
    path('5/<str:param>', views.templates2),
    path('6/', views.is_it_monday),
    path('7/', views.fruits),
]
