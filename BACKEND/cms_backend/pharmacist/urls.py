from django.urls import path
from . import views

urlpatterns = [
    path('api/medicines', views.MedicineListCreateAPIView.as_view(), name='medicine-list-create'),
    path('api/pharmacy/generate-bill', views.GeneratePharmacyBillAPIView.as_view(), name='generate-pharmacy-bill'),
]