from django.db import models
from administrator.models import TblDoctor
# Create your models here.

class LabTechnician(models.Model):
    lab_technician_id = models.AutoField(primary_key=True)
    technician_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    qualification = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "TblLabTechnician"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LabTestCategory(models.Model):
    lab_test_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "TblLabTestCategory"

    def __str__(self):
        return self.category_name


class LabTest(models.Model):
    lab_test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference_min_range = models.CharField(max_length=50)
    reference_max_range = models.CharField(max_length=50)
    sample_required = models.CharField(max_length=50)
    lab_test_category = models.ForeignKey(
        LabTestCategory,
        on_delete=models.CASCADE,
        db_column="LabTestCategoryId",
        related_name="lab_tests"
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "TblLabTest"

    def __str__(self):
        return self.test_name


class LabTestPrescription(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )

    lab_test_prescription_id = models.AutoField(primary_key=True)

    appointment = models.ForeignKey(
        "labtechnician.Appointment",
        on_delete=models.CASCADE,
        db_column="AppointmentId"
    )

    lab_test = models.ForeignKey(
        LabTest,
        on_delete=models.CASCADE,
        db_column="LabTestId"
    )

    assigned_lab_technician = models.ForeignKey(
        LabTechnician,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="AssignedLabTechnicianId"
    )

    prescription_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TblLabTestPrescription"

    def __str__(self):
        return f"{self.lab_test.test_name}"


class LabTestResult(models.Model):
    STATUS_CHOICES = (
        ("Completed", "Completed"),
        ("Verified", "Verified"),
    )

    lab_test_result_id = models.AutoField(primary_key=True)

    lab_test_prescription = models.OneToOneField(
        LabTestPrescription,
        on_delete=models.CASCADE,
        db_column="LabTestPrescriptionId"
    )

    lab_technician = models.ForeignKey(
        LabTechnician,
        on_delete=models.SET_NULL,
        null=True,
        db_column="LabTechnicianId"
    )

    result_value = models.TextField()
    remarks = models.TextField(blank=True, null=True)

    upload_image = models.ImageField(
        upload_to="lab_results/",
        blank=True,
        null=True
    )

    completed_on = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Completed"
    )

    class Meta:
        db_table = "TblLabTestResult"

    def __str__(self):
        return f"Result {self.lab_test_result_id}"
    
#---------------------------------------------------
# Appointment - just added for references
#---------------------------------------------------

class Appointment(models.Model):

    appointment_id = models.AutoField(primary_key=True)

    doctor = models.ForeignKey(
        TblDoctor,
        on_delete=models.CASCADE,
        db_column="DoctorId"
    )

    appointment_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        default="Scheduled"
    )

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "TblAppointment"