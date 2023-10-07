from django.db import models
from accounts.models import User


class Department(models.Model):
    doctor_id = models.ForeignKey(User, related_name='department', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=1000)
    diagnostics = models.TextField()
    location = models.CharField(max_length=1000)
    specialization = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.doctor_id}-{self.name}"


class PatientRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User, related_name='patient_record', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatment = models.TextField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.record_id}-{self.patient_id}"
    
