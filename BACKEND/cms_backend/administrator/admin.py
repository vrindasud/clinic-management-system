from django.contrib import admin

from .models import TblRole, TblSpecialization, TblStaff, TblDoctor


admin.site.register(TblRole)
admin.site.register(TblSpecialization)
admin.site.register(TblStaff)
admin.site.register(TblDoctor)
