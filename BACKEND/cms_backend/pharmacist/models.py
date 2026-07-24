from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator

class TblMedicineCategory(models.Model):
    MedicineCategoryId = models.AutoField(primary_key=True)
    MedicineCategoryName = models.CharField(max_length=100, unique=True)
    IsActive = models.IntegerField(default=1)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TblMedicineCategory'
        verbose_name = "Medicine Category"
        verbose_name_plural = "Medicine Categories"

    def __str__(self):
        return self.MedicineCategoryName

class TblMedicine(models.Model):
    MedicineId = models.AutoField(primary_key=True)
    MedicineCategoryId = models.ForeignKey(TblMedicineCategory, on_delete=models.PROTECT, db_column='MedicineCategoryId')
    MedicineName = models.CharField(max_length=255)
    MedicineForm = models.CharField(max_length=50)  # STRIP_CAPSULE, OINTMENT, SYRUP
    CapsulesPerStrip = models.IntegerField(null=True, blank=True)
    StripPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    BaseUnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ManufacturingDate = models.DateField()
    ExpiryDate = models.DateField()
    IsActive = models.IntegerField(default=1)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TblMedicine'
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"

    def __str__(self):
        return self.MedicineName

class TblMedicineStock(models.Model):
    MedicineStockId = models.AutoField(primary_key=True)
    MedicineId = models.OneToOneField(TblMedicine, on_delete=models.PROTECT, db_column='MedicineId')
    TotalUnitsRemaining = models.IntegerField(default=0)
    ReOrderLevel = models.IntegerField(default=10)
    IsActive = models.IntegerField(default=1)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TblMedicineStock'
        verbose_name = "Medicine Stock"
        verbose_name_plural = "Medicine Stocks"

    def __str__(self):
        return f"Stock for {self.MedicineId.MedicineName} ({self.TotalUnitsRemaining} units)"

class TblPrescriptionBill(models.Model):
    BillId = models.AutoField(primary_key=True)
    AppointmentId = models.IntegerField()  
    PatientId = models.IntegerField()      
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    IsPaid = models.IntegerField(default=0)
    IsActive = models.IntegerField(default=1)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TblPrescriptionBill'
        verbose_name = "Prescription Bill"
        verbose_name_plural = "Prescription Bills"

    def __str__(self):
        return f"Bill #{self.BillId} - Patient {self.PatientId} (Total: {self.TotalAmount})"

class TblPrescriptionBillItem(models.Model):
    BillItemId = models.AutoField(primary_key=True)
    BillId = models.ForeignKey(TblPrescriptionBill, on_delete=models.CASCADE, db_column='BillId', related_name='items')
    MedicineId = models.ForeignKey(TblMedicine, on_delete=models.PROTECT, db_column='MedicineId')
    StripsBilled = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    CapsulesBilled = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    FlatUnitsBilled = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ItemCalculatedAmount = models.DecimalField(max_digits=10, decimal_places=2)
    IsActive = models.IntegerField(default=1)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedOn = models.DateTimeField(auto_now=True, null=True)
    UpdatedBy = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'TblPrescriptionBillItem'
        verbose_name = "Prescription Bill Item"
        verbose_name_plural = "Prescription Bill Items"

    def __str__(self):
        return f"Item #{self.BillItemId} in Bill #{self.BillId.BillId} ({self.MedicineId.MedicineName})"