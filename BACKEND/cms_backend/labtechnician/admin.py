from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (
    LabTechnician,
    LabTestCategory,
    LabTest,
    Appointment,
    LabTestPrescription,
    LabTestResult
)

admin.site.register(LabTechnician)
admin.site.register(LabTestCategory)
admin.site.register(LabTest)
admin.site.register(Appointment)
admin.site.register(LabTestPrescription)
admin.site.register(LabTestResult)