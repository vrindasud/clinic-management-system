from django.contrib import admin
from .models import TblMedicineCategory, TblMedicine, TblMedicineStock, TblPrescriptionBill, TblPrescriptionBillItem

# Change the main Admin Panel Titles
admin.site.site_header = "Clinic Management - Pharmacy System"
admin.site.site_title = "Pharmacy Admin Portal"
admin.site.index_title = "Welcome to the Pharmacy Dashboard"

@admin.register(TblMedicine)
class MedicineAdmin(admin.ModelAdmin):
    # This changes what columns show up in the main list table
    list_display = ('MedicineName', 'MedicineForm', 'BaseUnitPrice', 'ExpiryDate', 'IsActive')
    
    # Adds a search bar at the top to find medicines instantly
    search_fields = ('MedicineName',)
    
    # Adds a filter sidebar on the right
    list_filter = ('MedicineForm', 'IsActive', 'MedicineCategoryId')
    
    # Organizes the input form fields into distinct, clean visual sections
    fieldsets = (
        ("Basic Details", {
            'fields': ('MedicineName', 'MedicineCategoryId', 'MedicineForm')
        }),
        ("Pricing & Packaging", {
            'fields': ('CapsulesPerStrip', 'StripPrice', 'BaseUnitPrice')
        }),
        ("Dates & Status", {
            'fields': ('ManufacturingDate', 'ExpiryDate', 'IsActive', 'UpdatedBy')
        }),
    )

# Register the remaining tables normally
admin.site.register(TblMedicineCategory)
admin.site.register(TblMedicineStock)
admin.site.register(TblPrescriptionBill)
admin.site.register(TblPrescriptionBillItem)