
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from decimal import Decimal
from .models import TblRole, TblSpecialization, TblStaff, TblDoctor


class TblRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblRole
        fields = '__all__'


class TblSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblSpecialization
        fields = '__all__'


class TblStaffSerializer(serializers.ModelSerializer):
    # Nested Serializer usage to fetch read-only details of the role object cleanly
    role_details = TblRoleSerializer(source='role_id', read_only=True)

    class Meta:
        model = TblStaff
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # Keeps hidden from client responses
        }

    # LEVEL 1 VALIDATION: Field Level Validation (using validate_<fieldname>)
    def validate_mobile_number(self, value):
        if value and len(str(value)) < 10:
            raise serializers.ValidationError("Mobile number format must be at least 10 digits long.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Secure hash string representation
        return super().create(validated_data)


class TblDoctorSerializer(serializers.ModelSerializer):
    # Nested Serializers to show combined staff and department records
    staff_details = TblStaffSerializer(source='staff_id', read_only=True)
    specialization_details = TblSpecializationSerializer(source='specialization_id', read_only=True)

    class Meta:
        model = TblDoctor
        fields = '__all__'

    # LEVEL 1 VALIDATION: Field Level Validation
    def validate_consultation_fee(self, value):
        if value < Decimal('0.00'):
            raise serializers.ValidationError("Consultation fee cannot be negative values.")
        return value

    # LEVEL 2 VALIDATION: Object Level Validation (compares multiple fields or handles cross-checks)
    def validate(self, data):
        staff_member = data.get('staff_id')
        is_active = data.get('is_active', True)

        # Cross-field rule check: Cannot launch active clinical setup profiles for inactive personnel
        if is_active and staff_member and not staff_member.is_active:
            raise serializers.ValidationError(
                "Cannot create or activate a Doctor profile for an inactive staff account.")

        return data