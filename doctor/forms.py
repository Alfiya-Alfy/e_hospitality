from django import forms
from django.contrib.auth.models import User
from patient.models import PatientHistory, Invoice
from .models import DoctorProfile
class DoctorRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    specialization = forms.CharField(required=False)
    experience = forms.IntegerField(required=False)
    contact_number = forms.CharField(required=False)
    qualifications = forms.CharField(widget=forms.Textarea, required=False)
    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        email=data.get('email') or '',
                                        password=data['password'],
                                        first_name=data.get('first_name') or '',
                                        last_name=data.get('last_name') or '')
        DoctorProfile.objects.create(user=user,
                                     specialization=data.get('specialization'),
                                     experience=data.get('experience') or 0,
                                     contact_number=data.get('contact_number'),
                                     qualifications=data.get('qualifications'))
        return user

class PatientHistoryForm(forms.ModelForm):
    class Meta:
        model = PatientHistory
        fields = ['patient', 'diagnosis', 'treatment', 'notes']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['patient', 'amount', 'description']
