from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import TblRole, TblSpecialization, TblStaff, TblDoctor
from .serializers import TblRoleSerializer, TblSpecializationSerializer, TblStaffSerializer, TblDoctorSerializer

class TblRoleViewSet(viewsets.ModelViewSet):
    queryset = TblRole.objects.all()
    serializer_class = TblRoleSerializer


class TblSpecializationViewSet(viewsets.ModelViewSet):
    queryset = TblSpecialization.objects.all()
    serializer_class = TblSpecializationSerializer


class TblStaffViewSet(viewsets.ModelViewSet):
    queryset = TblStaff.objects.all()
    serializer_class = TblStaffSerializer

    # Filters, Ordering, and Search Setup Configurations
    filterset_fields = ['role_id', 'is_active', 'city']
    search_fields = ['full_name', 'user_name', 'email']
    ordering_fields = ['joining_date', 'full_name']

    @action(detail=True, methods=['patch'], url_path='deactivate')
    def deactivate(self, request, pk=None):
        staff = self.get_object()
        staff.is_active = False
        staff.save()
        return Response({"message": "Staff account has been deactivated successfully."}, status=status.HTTP_200_OK)


class TblDoctorViewSet(viewsets.ModelViewSet):
    queryset = TblDoctor.objects.all()
    serializer_class = TblDoctorSerializer

    filterset_fields = ['specialization_id', 'is_active']
    search_fields = ['staff_id__full_name'] # Search through related table models
    ordering_fields = ['consultation_fee']

    @action(detail=True, methods=['patch'], url_path='deactivate')
    def deactivate(self, request, pk=None):
        doctor = self.get_object()
        doctor.is_active = False
        doctor.save()
        return Response({"message": "Practitioner's availability has been disabled."}, status=status.HTTP_200_OK)