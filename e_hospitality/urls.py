from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('patient:home')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('patient/', include(('patient.urls','patient'), namespace='patient')),
    path('doctor/', include(('doctor.urls','doctor'), namespace='doctor')),
]
