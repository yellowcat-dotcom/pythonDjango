from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Doctor, Patient, AppointmentJournal
from .forms import DoctorForm, DoctorListForm, DoctorUpdateForm
from .forms import PatientForm, PatientListForm, PatientUpdateForm
from .forms import AppointmentJournalForm, AppointmentJournalListForm, AppointmentJournalUpdateForm


def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'create_form.html', {'form': form, 'model_name': 'Doctor'})


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'list_form.html', {'objects': doctors, 'model_name': 'Doctor'})


def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorUpdateForm(instance=doctor)
    return render(request, 'update_form.html', {'form': form, 'model_name': 'Doctor'})


def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'delete_confirm.html', {'object': doctor, 'model_name': 'Doctor'})


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'create_form.html', {'form': form, 'model_name': 'Patient'})


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'list_form.html', {'objects': patients, 'model_name': 'Patient'})


def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientUpdateForm(instance=patient)
    return render(request, 'update_form.html', {'form': form, 'model_name': 'Patient'})


def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'delete_confirm.html', {'object': patient, 'model_name': 'Patient'})


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentJournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentJournalForm()
    return render(request, 'create_form.html', {'form': form, 'model_name': 'Appointment Journal'})


def appointment_list(request):
    appointments = AppointmentJournal.objects.all()
    return render(request, 'list_form.html', {'objects': appointments, 'model_name': 'Appointment Journal'})


def update_appointment(request, pk):
    appointment = get_object_or_404(AppointmentJournal, pk=pk)
    if request.method == 'POST':
        form = AppointmentJournalUpdateForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentJournalUpdateForm(instance=appointment)
    return render(request, 'update_form.html', {'form': form, 'model_name': 'Appointment Journal'})


def delete_appointment(request, pk):
    appointment = get_object_or_404(AppointmentJournal, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'delete_confirm.html', {'object': appointment, 'model_name': 'Appointment Journal'})
