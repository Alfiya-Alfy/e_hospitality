from django.urls import path
from . import views

app_name = 'doctor'
urlpatterns = [
    path('register/', views.register_doctor, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.doctor_profile, name='profile'),
    path('add-history/', views.add_history, name='add_history'),
    path('create-invoice/', views.create_invoice, name='create_invoice'),
]
