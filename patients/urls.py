from django.urls import path
from .views import PatientsClinicMasterList,PatientsClinicMasterDetail,TherapyPatient
app_name = "patients"
urlpatterns = [
    path("patients_search/", PatientsClinicMasterList.as_view(), name="patient_search"),
    path('create/', TherapyPatient.as_view(), name="create"),
    path('detail/<str:pk>/', PatientsClinicMasterDetail.as_view(), name="detail"),
]
