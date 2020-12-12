from django.urls import path

from auth_intro import views

app_name = "auth"

urlpatterns = [
    path('cookie/', views.cookie, name="cookie"),
    path('session/', views.session, name="session"),
]