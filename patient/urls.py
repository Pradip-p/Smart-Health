from django.contrib import admin
from django.urls import path,include
from patient import views
from django.views.generic.base import RedirectView

urlpatterns = [        
path('patient/',RedirectView.as_view(url='patient_login/')),
path('patient_login/', views.patient_login,name='patient_login'),
path('patient_register/', views.patient_register,name='patient_register'),
path('dashboard/', views.dashboard, name="dashboard"),
path('logoutpatient/', views.logoutpatient, name="logoutpatient")
]