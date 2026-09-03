from django.shortcuts import render
from rest_framework import viewsets
from .models import LabTechnician, LabTestCategory, LabTest, LabTestPrescription, LabTestResult, Appointment
from .serializers import LabTechnicianSerializer, LabTestCategorySerializer, LabTestSerializer, LabTestPrescriptionSerializer, LabTestResultSerializer, AppointmentSerializer
# Create your views here.

class LabTechnicianViewSet(viewsets.ModelViewSet):
    queryset = LabTechnician.objects.all()
    serializer_class = LabTechnicianSerializer


class LabTestCategoryViewSet(viewsets.ModelViewSet):
    queryset = LabTestCategory.objects.all()
    serializer_class = LabTestCategorySerializer


class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class LabTestPrescriptionViewSet(viewsets.ModelViewSet):
    queryset = LabTestPrescription.objects.all()
    serializer_class = LabTestPrescriptionSerializer


class LabTestResultViewSet(viewsets.ModelViewSet):
    queryset = LabTestResult.objects.all()
    serializer_class = LabTestResultSerializer