from .models import *
from rest_framework import serializers
from accounts.models import User

class ViewUsers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PatientRecordSerializer(serializers.ModelSerializer):
    department_id = DepartmentSerializer()
    patient_id = ViewUsers()
    class Meta:
        model = PatientRecord
        fields = '__all__'


class DoctorViewSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'department']
    
    def get_department(self, obj):
        department = obj.department.get()

        if department:
            return DepartmentSerializer(department).data
        return None


class PatientViewSerializer(serializers.ModelSerializer):
    record = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'record']
    
    def get_record(self, obj):
        record = obj.patient_record.get()

        if record:
            return PatientRecordSerializer(record).data
        return None