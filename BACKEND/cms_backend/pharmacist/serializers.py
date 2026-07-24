from rest_framework import serializers
from .models import TblMedicineCategory, TblMedicine, TblMedicineStock, TblPrescriptionBill, TblPrescriptionBillItem

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblMedicine
        fields = '__all__'

class PrescriptionBillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblPrescriptionBillItem
        fields = '__all__'

class PrescriptionBillSerializer(serializers.ModelSerializer):
    items = PrescriptionBillItemSerializer(many=True, read_only=True)

    class Meta:
        model = TblPrescriptionBill
        fields = '__all__'