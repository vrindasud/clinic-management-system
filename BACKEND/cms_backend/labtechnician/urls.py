from rest_framework.routers import DefaultRouter

from .views import (
    LabTechnicianViewSet,
    LabTestCategoryViewSet,
    LabTestViewSet,
    AppointmentViewSet,
    LabTestPrescriptionViewSet,
    LabTestResultViewSet
)

router = DefaultRouter()

router.register(
    r'lab-technicians',
    LabTechnicianViewSet
)

router.register(
    r'lab-test-categories',
    LabTestCategoryViewSet
)

router.register(
    r'lab-tests',
    LabTestViewSet
)

router.register(
    r'appointments',
    AppointmentViewSet
)

router.register(
    r'lab-test-prescriptions',
    LabTestPrescriptionViewSet
)

router.register(
    r'lab-test-results',
    LabTestResultViewSet
)

urlpatterns = router.urls