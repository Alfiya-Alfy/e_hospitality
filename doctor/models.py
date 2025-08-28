from django.db import models
from django.contrib.auth.models import User

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    def __str__(self): return f"Dr. {self.user.username} - {self.specialization or 'General'}"

class Facility(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    def __str__(self): return self.name

class HealthEducationResource(models.Model):
    CATEGORY_CHOICES = (
        ('diet', 'Diet & Nutrition'),
        ('exercise', 'Exercise & Fitness'),
        ('mental', 'Mental Health'),
        ('disease', 'Disease Awareness'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
