from rest_framework import serializers
from clinicmaster.models import Patients
from .models import Patient

class PatientsClinicMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"
    


class PatientsTherapySerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        