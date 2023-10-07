from rest_framework.permissions import BasePermission
from accounts.models import User
from .models import Department


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Doctors').exists()


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        pk = view.kwargs.get('pk')
        return pk == request.user.pk


class ThePatientOrDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        pk = view.kwargs.get('pk')
        user_department = request.user.department.get().id
        patient = User.objects.get(pk=pk)
        try:
            patient_department = patient.patient_record.get().department_id.id
        except:
            patient_department = None

        if request.user.groups.filter(name='Patients').exists() and pk == request.user.pk:
            return True
        elif request.user.groups.filter(name='Doctors').exists() and user_department == patient_department:
            return True
        return False


class SameDepartment(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        pk = view.kwargs.get('pk')
        department = Department.objects.get(pk=pk).name
        user_department_id = request.user.department.get().name
        if department == user_department_id:
            return True
        return False