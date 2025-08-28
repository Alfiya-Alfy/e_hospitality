from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment, MedicalRecord, Invoice, PatientHistory, PatientProfile
from .forms import AppointmentForm, MedicalRecordForm, PatientRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from doctor.models import HealthEducationResource, Facility

from django.db import transaction, IntegrityError


def register_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()   # your form.save should create User + PatientProfile
                messages.success(request, 'Patient registered successfully. Please login.')
                return redirect('login')
            except IntegrityError:
                # This handles a race-condition or duplicate username
                form.add_error('username', 'Username already exists — please choose another.')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/register.html', {'form': form})
@login_required
def home(request):
    # redirect doctors to doctor dashboard
    if hasattr(request.user, 'doctorprofile'):
        return redirect('doctor:dashboard')
    appts = Appointment.objects.filter(patient=request.user).order_by('-date')
    invoices = Invoice.objects.filter(patient=request.user)
    histories = PatientHistory.objects.filter(patient=request.user).order_by('-date')
    resources = HealthEducationResource.objects.all()
    facilities = Facility.objects.all()
    return render(request, 'patient/home.html', {'appointments': appts, 'invoices': invoices, 'histories': histories, 'resources': resources, 'facilities': facilities})

@login_required
def appointment_list(request):
    appts = Appointment.objects.filter(patient=request.user).order_by('-date')
    return render(request, 'patient/appointment_list.html', {'appointments': appts})

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.patient = request.user
            appt.save()
            messages.success(request, 'Appointment created.')
            return redirect('patient:appointment_list')
    else:
        form = AppointmentForm()
        form.fields['doctor'].queryset = User.objects.filter(doctorprofile__isnull=False)
    return render(request, 'patient/appointment_create.html', {'form': form})

@login_required
def medical_history(request):
    records = MedicalRecord.objects.filter(patient=request.user).order_by('-created_at')
    return render(request, 'patient/medical_history.html', {'records': records})

@login_required
def pay_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id, patient=request.user)
    invoice.paid = True
    invoice.save()
    messages.success(request, "Invoice marked as paid.")
    return redirect('patient:home')

@login_required
def patient_profile(request):
    profile = getattr(request.user, 'patientprofile', None)
    medical_records = MedicalRecord.objects.filter(patient=request.user)
    histories = PatientHistory.objects.filter(patient=request.user)
    invoices = Invoice.objects.filter(patient=request.user)
    resources = HealthEducationResource.objects.all()
    facilities = Facility.objects.all()
    return render(request, 'patient/profile.html', {
        'profile': profile,
        'medical_records': medical_records,
        'histories': histories,
        'invoices': invoices,
        'resources': resources,
        'facilities': facilities,
    })
