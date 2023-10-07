from django.urls import path
from .views import *


urlpatterns = [
    path('doctors/', DoctorsView.as_view(), name='doctors-view'),
    path('doctors/<int:pk>', view_doctor_info, name='doctor-view-single'),
    path('patients/', PatientView.as_view(), name='patient-view'),
    path('patients/<int:pk>', view_patient_info, name='patient-view-single'),
    path('patient_records/', PatientsRecordView.as_view(), name='patient-record-view'),
    path('patient_records/<int:pk>', view_patient_record, name='patient-record-view-single'),
    path('department/', DepartmentView.as_view(), name='department-view'),
    path('department/<int:pk>/doctors', DepartmentDoctorView.as_view(), name='department-doctor-view'),
    path('department/<int:pk>/patients', DepartmentPatientView.as_view(), name='department-patient-view'),
]
