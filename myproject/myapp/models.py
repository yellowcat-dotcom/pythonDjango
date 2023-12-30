from django.db import models


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.last_name} {self.first_name} {self.middle_name}"


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.last_name} {self.first_name} {self.middle_name}"


class AppointmentJournal(models.Model):
    id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()

    def __str__(self):
        return f"ID - {self.id} Appointment {self.id} - Doctor: {self.doctor}, Patient: {self.patient}, Date: {self.appointment_date}"
