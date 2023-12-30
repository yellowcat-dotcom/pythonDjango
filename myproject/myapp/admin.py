from django.contrib import admin
from .models import Doctor, AppointmentJournal, Patient

admin.site.register(Doctor)
admin.site.register(AppointmentJournal)
admin.site.register(Patient)