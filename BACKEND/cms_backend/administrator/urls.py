from rest_framework.routers import DefaultRouter
from .views import TblRoleViewSet, TblSpecializationViewSet, TblStaffViewSet, TblDoctorViewSet

router = DefaultRouter(trailing_slash=False)
router.register('roles', TblRoleViewSet, basename='roles')
router.register('specializations', TblSpecializationViewSet, basename='specializations')
router.register('staff', TblStaffViewSet, basename='staff')
router.register('doctors', TblDoctorViewSet, basename='doctors')

urlpatterns = router.urls
