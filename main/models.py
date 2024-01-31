from django.db import models
from clinicmaster.models import Patients
import django_filters


class PatientsClinicMasterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    
    class Meta:
        model = Patients
        fields = ["patientno",]