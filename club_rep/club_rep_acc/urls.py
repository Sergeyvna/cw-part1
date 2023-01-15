from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.bookings, name='bookings'),
    path('account/', views.account, name='account'),
    path('create_rep/', views.create_rep, name='create_rep'),
    path('update_rep/<str:pk>/', views.update, name='update_rep'),
    path('delete_rep/<str:pk>/', views.delete, name='delete_rep'),
]