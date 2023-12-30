import re  # для регулярок
from django import forms
from .models import Doctor, Patient, AppointmentJournal


def validate_name(name):
    regex_pattern = r'^[А-ЯЁ][а-яё]+$'
    return bool(re.match(regex_pattern, name))


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not validate_name(last_name):
            raise forms.ValidationError("Фамилия должна начинаться с прописной буквы и содержать буквы на кириллице.")
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not validate_name(first_name):
            raise forms.ValidationError("Имя должно начинаться с прописной буквы и содержать буквы на кириллице.")
        return first_name

    def clean_middle_name(self):
        middle_name = self.cleaned_data['middle_name']
        if not validate_name(middle_name):
            raise forms.ValidationError("Отчество должно начинаться с прописной буквы и содержать буквы на кириллице.")
        return middle_name


class DoctorListForm(forms.Form):
    pass  # Нет необходимости в форме для вывода всех записей


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not validate_name(last_name):
            raise forms.ValidationError("Фамилия должна начинаться с прописной буквы и содержать буквы на кириллице.")
        return last_name

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not validate_name(first_name):
            raise forms.ValidationError("Имя должно начинаться с прописной буквы и содержать буквы на кириллице.")
        return first_name

    def clean_middle_name(self):
        middle_name = self.cleaned_data['middle_name']
        if not validate_name(middle_name):
            raise forms.ValidationError("Отчество должно начинаться с прописной буквы и содержать буквы на кириллице.")
        return middle_name


class PatientListForm(forms.Form):
    pass  # Нет необходимости в форме для вывода всех записей


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentJournalForm(forms.ModelForm):
    class Meta:
        model = AppointmentJournal
        fields = '__all__'


class AppointmentJournalListForm(forms.Form):
    pass  # Нет необходимости в форме для вывода всех записей


class AppointmentJournalUpdateForm(forms.ModelForm):
    class Meta:
        model = AppointmentJournal
        fields = '__all__'
