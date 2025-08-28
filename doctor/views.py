from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DoctorProfile, Facility, HealthEducationResource
from .forms import DoctorRegistrationForm, PatientHistoryForm, InvoiceForm
from django.contrib import messages
from patient.models import PatientHistory, Invoice
from django.contrib.auth.models import User

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor registered. Please login.')
            return redirect('login')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'doctor/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = getattr(request.user, 'doctorprofile', None)
    if not profile:
        return render(request, 'doctor/not_doctor.html', {'msg':'You are not registered as doctor.'})
    facilities = Facility.objects.all()
    resources = HealthEducationResource.objects.all()
    # appointments and prescriptions may be created/queried here
    return render(request, 'doctor/dashboard.html', {'profile': profile, 'facilities': facilities, 'resources': resources})

@login_required
def doctor_profile(request):
    profile = getattr(request.user, 'doctorprofile', None)
    return render(request, 'doctor/profile.html', {'profile': profile})

@login_required
def add_history(request):
    profile = getattr(request.user, 'doctorprofile', None)
    if not profile:
        messages.error(request, 'Only doctors can add history.')
        return redirect('doctor:dashboard')
    if request.method == 'POST':
        form = PatientHistoryForm(request.POST)
        if form.is_valid():
            ph = form.save(commit=False)
            ph.doctor = request.user
            ph.save()
            messages.success(request, 'Patient history added.')
            return redirect('doctor:dashboard')
    else:
        form = PatientHistoryForm()
    return render(request, 'doctor/add_history.html', {'form': form})

@login_required
def create_invoice(request):
    profile = getattr(request.user, 'doctorprofile', None)
    if not profile:
        messages.error(request, 'Only doctors can create invoices.')
        return redirect('doctor:dashboard')
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            messages.success(request, 'Invoice created.')
            return redirect('doctor:dashboard')
    else:
        form = InvoiceForm()
    return render(request, 'doctor/create_invoice.html', {'form': form})
