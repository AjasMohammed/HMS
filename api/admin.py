from django.contrib import admin
from .models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'doctor_id':
            kwargs['queryset'] = User.objects.filter(groups__name='Doctors')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(PatientRecord)
class PatientRecordAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'patient_id':
            kwargs['queryset'] = User.objects.filter(groups__name='Patients')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

