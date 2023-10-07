from .models import *
from .serializers import *
from accounts.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .custom_permission import IsDoctor, IsOwner, ThePatientOrDoctor, SameDepartment
from rest_framework.response import Response
from accounts.models import User


class DoctorsView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        doctors = User.objects.filter(groups__name='Doctors')
        serializer = ViewUsers(doctors, many=True)
        return Response(serializer.data)


class PatientView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        patients = User.objects.filter(groups__name='Patients')
        serializer = ViewUsers(patients, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsDoctor, IsOwner))
def view_doctor_info(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = DoctorViewSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data = request.data, partial=True)
        if not serializer.is_valid():
            return Response({"message": "invalid data!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "user deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, ThePatientOrDoctor))
def view_patient_info(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        p = User.objects.get(pk=pk)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data = request.data, partial=True)
        if not serializer.is_valid():
            return Response({"message": "invalid data!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "user deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class PatientsRecordView(ListAPIView):
    serializer_class = PatientRecordSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

    def get_queryset(self):
        user = self.request.user
        department = user.department.get()
        queryset = PatientRecord.objects.filter(department_id=department)
        return queryset
    


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, ThePatientOrDoctor))
def view_patient_record(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = PatientViewSerializer(user)

        p = User.objects.get(pk=pk)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data = request.data, partial=True)
        if not serializer.is_valid():
            return Response({"message": "invalid data!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({"message": "data updated successfully!", "data": serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response({"message": "user deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class DepartmentView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]


class DepartmentDoctorView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor, SameDepartment]
    def get(self, request, pk):

        user_department = request.user.department.get().name
        departments = Department.objects.filter(name=user_department)
        doctors = [department.doctor_id for department in departments]
        serializer = DoctorViewSerializer(doctors, many=True)
        return Response(serializer.data)


class DepartmentPatientView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor, SameDepartment]
    
    def get(self, request, pk):
        user_department = request.user.department.get().name
        departments = Department.objects.filter(name=user_department)
        p = PatientRecord.objects.filter(department_id__in=departments)
        print(p)
        s = PatientRecordSerializer(p, many=True)
        
        return Response(s.data)