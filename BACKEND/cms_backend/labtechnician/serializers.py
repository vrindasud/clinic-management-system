from rest_framework import serializers
from .models import LabTechnician, LabTestPrescription, LabTestResult, LabTestCategory, LabTest, Appointment

# create serializers

class LabTechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTechnician
        fields = '__all__'

class LabTestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestCategory
        fields = '__all__'

class LabTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = '__all__'

class LabTestPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestPrescription
        fields = '__all__'

class LabTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestResult
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'