from django.contrib import admin
from .models import DoctorProfile, Facility, HealthEducationResource
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience')
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
@admin.register(HealthEducationResource)
class HealthEducationResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
