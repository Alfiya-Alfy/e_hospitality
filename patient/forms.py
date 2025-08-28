from django import forms
from django.contrib.auth.models import User
from .models import PatientProfile, Appointment, MedicalRecord
class PatientRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    contact_number = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    age = forms.IntegerField(required=False)
    gender = forms.CharField(required=False)
    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        email=data.get('email') or '',
                                        password=data['password'],
                                        first_name=data.get('first_name') or '',
                                        last_name=data.get('last_name') or '')
        PatientProfile.objects.create(user=user,
                                      contact_number=data.get('contact_number'),
                                      address=data.get('address'),
                                      age=data.get('age'),
                                      gender=data.get('gender'))
        return user

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'reason']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['title', 'description']
