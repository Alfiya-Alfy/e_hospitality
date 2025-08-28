from django.db import models
from django.contrib.auth.models import User

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=32, blank=True, null=True)
    def __str__(self): return f"Patient: {self.user.username}"

class Appointment(models.Model):
    STATUS_CHOICES = (('scheduled','Scheduled'), ('cancelled','Cancelled'), ('done','Done'))
    patient = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor_appointments', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Appt: {self.patient.username} with {self.doctor.username if self.doctor else 'TBD'} on {self.date}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(User, related_name='medical_records', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.title} - {self.patient.username}"

class Invoice(models.Model):
    patient = models.ForeignKey(User, related_name='invoices', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Invoice {self.id} - {self.patient.username} - {self.amount}"

class PatientHistory(models.Model):
    patient = models.ForeignKey(User, related_name='history_records', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='history_as_doctor', on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self): return f"History of {self.patient.username} on {self.date}"
