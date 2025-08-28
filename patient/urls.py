from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_patient, name='register'),
    path('profile/', views.patient_profile, name='profile'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('medical-history/', views.medical_history, name='medical_history'),
    path('invoice/<int:invoice_id>/pay/', views.pay_invoice, name='pay_invoice'),
]
