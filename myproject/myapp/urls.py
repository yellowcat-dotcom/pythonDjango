from django.contrib import admin
from django.urls import path
from .views import create_doctor, doctor_list, update_doctor, delete_doctor
from .views import create_patient, patient_list, update_patient, delete_patient
from .views import create_appointment, appointment_list, update_appointment, delete_appointment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/doctor/', create_doctor, name='create_doctor'),
    path('list/doctor/', doctor_list, name='doctor_list'),
    path('update/doctor/<int:pk>/', update_doctor, name='update_doctor'),
    path('delete/doctor/<int:pk>/', delete_doctor, name='delete_doctor'),

    path('create/patient/', create_patient, name='create_patient'),
    path('list/patient/', patient_list, name='patient_list'),
    path('update/patient/<int:pk>/', update_patient, name='update_patient'),
    path('delete/patient/<int:pk>/', delete_patient, name='delete_patient'),

    path('create/appointment/', create_appointment, name='create_appointment'),
    path('list/appointment/', appointment_list, name='appointment_list'),
    path('update/appointment/<int:pk>/', update_appointment, name='update_appointment'),
    path('delete/appointment/<int:pk>/', delete_appointment, name='delete_appointment'),


]
