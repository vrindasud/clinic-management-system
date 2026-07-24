from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import TblMedicine, TblMedicineStock, TblPrescriptionBill, TblPrescriptionBillItem
from .serializers import MedicineSerializer, PrescriptionBillSerializer

class MedicineListCreateAPIView(generics.ListCreateAPIView):
    queryset = TblMedicine.objects.filter(IsActive=1)
    serializer_class = MedicineSerializer

class GeneratePharmacyBillAPIView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        items_payload = data.get('Items', [])
        
        if not items_payload:
            return Response({"error": "No checkout line items provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        bill = TblPrescriptionBill.objects.create(
            AppointmentId=data['AppointmentId'],
            PatientId=data['PatientId'],
            UpdatedBy=data.get('StaffId'),
            TotalAmount=0.00
        )
        
        running_grand_total = 0
        
        for item in items_payload:
            medicine = get_object_or_404(TblMedicine, pk=item['MedicineId'], IsActive=1)
            stock_record = get_object_or_404(TblMedicineStock, MedicineId=medicine)
            
            strips = int(item.get('StripsBilled', 0))
            capsules = int(item.get('CapsulesBilled', 0))
            flat_units = int(item.get('FlatUnitsBilled', 0))
            
            if medicine.MedicineForm == 'STRIP_CAPSULE':
                requested_units = (strips * (medicine.CapsulesPerStrip or 0)) + capsules
            else:
                requested_units = flat_units
            
            if stock_record.TotalUnitsRemaining < requested_units:
                transaction.set_rollback(True)
                return Response({
                    "error": f"Insufficient stock for {medicine.MedicineName}. Available units: {stock_record.TotalUnitsRemaining}"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if medicine.MedicineForm == 'STRIP_CAPSULE':
                line_cost = (strips * (medicine.StripPrice or 0)) + (capsules * medicine.BaseUnitPrice)
            else:
                line_cost = flat_units * medicine.BaseUnitPrice
                
            TblPrescriptionBillItem.objects.create(
                BillId=bill,
                MedicineId=medicine,
                StripsBilled=strips,
                CapsulesBilled=capsules,
                FlatUnitsBilled=flat_units,
                ItemCalculatedAmount=line_cost,
                UpdatedBy=data.get('StaffId')
            )
            
            stock_record.TotalUnitsRemaining -= requested_units
            stock_record.save()
            
            running_grand_total += line_cost
            
        bill.TotalAmount = running_grand_total
        bill.save()
        
        return Response({
            "message": "Pharmacy bill generated successfully",
            "BillId": bill.BillId,
            "TotalAmount": float(bill.TotalAmount)
        }, status=status.HTTP_201_CREATED)