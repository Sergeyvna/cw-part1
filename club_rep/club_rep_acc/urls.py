from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('films/', views.cinemas),
    path('account/', views.account),
]