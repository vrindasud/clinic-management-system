from django.db import models

# Create your models here.



class TblRole(models.Model):
    role_id = models.AutoField(primary_key=True, db_column='RoleId')
    role_name = models.CharField(max_length=30, unique=True, db_column='RoleName')
    is_active = models.BooleanField(default=True, db_column='IsActive')
    created_on = models.DateTimeField(null=True, blank=True, db_column='CreatedOn')
    updated_on = models.DateTimeField(null=True, blank=True, db_column='UpdatedOn')
    updated_by = models.IntegerField(null=True, blank=True, db_column='UpdatedBy')

    class Meta:
        db_table = 'TblRole'

    def __str__(self):
        return self.role_name


class TblSpecialization(models.Model):
    specialization_id = models.AutoField(primary_key=True, db_column='SpecializationId')
    specialization_name = models.CharField(max_length=30, unique=True, db_column='SpecializationName')
    is_active = models.BooleanField(default=True, db_column='IsActive')
    created_on = models.DateTimeField(null=True, blank=True, db_column='CreatedOn')
    updated_on = models.DateTimeField(null=True, blank=True, db_column='UpdatedOn')
    updated_by = models.IntegerField(null=True, blank=True, db_column='UpdatedBy')

    class Meta:
        db_table = 'TblSpecialization'

    def __str__(self):
        return self.specialization_name


class TblStaff(models.Model):
    staff_id = models.AutoField(primary_key=True, db_column='StaffId')
    full_name = models.CharField(max_length=100, db_column='FullName')
    gender = models.CharField(max_length=1, db_column='Gender')  
    joining_date = models.DateField(null=True, blank=True, db_column='JoiningDate')
    address_line_1 = models.CharField(max_length=100, null=True, blank=True, db_column='Address Line 1')
    address_line_2 = models.CharField(max_length=100, null=True, blank=True, db_column='Address Line 2')
    city = models.CharField(max_length=50, null=True, blank=True, db_column='City')
    pincode = models.CharField(max_length=20, null=True, blank=True, db_column='Pincode')
    mobile_number = models.CharField(max_length=20, unique=True, null=True, blank=True, db_column='MobileNumber')
    email = models.CharField(max_length=255, null=True, blank=True, db_column='Email')
    user_name = models.CharField(max_length=30, unique=True, db_column='UserName')
    password = models.CharField(max_length=255, db_column='Password')

    # Foreign Key Relationship to TblRole
    role_id = models.ForeignKey(
        TblRole,
        on_delete=models.PROTECT,
        db_column='RoleId'
    )

    is_active = models.BooleanField(default=True, db_column='IsActive')
    created_on = models.DateTimeField(null=True, blank=True, db_column='CreatedOn')
    updated_on = models.DateTimeField(null=True, blank=True, db_column='UpdatedOn')
    updated_by = models.IntegerField(null=True, blank=True, db_column='UpdatedBy')

    class Meta:
        db_table = 'TblStaff'

    def __str__(self):
        return self.full_name


class TblDoctor(models.Model):
    doctor_id = models.AutoField(primary_key=True, db_column='DoctorId')
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, db_column='ConsultationFee')

    # Foreign Key Relationship to TblSpecialization
    specialization_id = models.ForeignKey(
        TblSpecialization,
        on_delete=models.PROTECT,
        db_column='SpecializationId'
    )

    # Foreign Key Relationship to TblStaff
    staff_id = models.ForeignKey(
        TblStaff,
        on_delete=models.CASCADE,
        db_column='StaffId'
    )

    is_active = models.BooleanField(default=True, db_column='IsActive')
    created_on = models.DateTimeField(null=True, blank=True, db_column='CreatedOn')
    updated_on = models.DateTimeField(null=True, blank=True, db_column='UpdatedOn')
    updated_by = models.IntegerField(null=True, blank=True, db_column='UpdatedBy')

    class Meta:
        db_table = 'TblDoctor'

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}"
