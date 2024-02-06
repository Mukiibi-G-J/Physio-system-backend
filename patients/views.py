from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters 
from rest_framework import views
from clinicmaster.models import Patients
from  main.models import  PatientsClinicMasterFilter
from .models import Patient
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PatientsClinicMasterSerializer, PatientsTherapySerializer
from rest_framework.response import Response
from physio.models import PhysioSessionAdmission
from django.core.exceptions import ImproperlyConfigured
from rest_framework import status
# def patient_search(request):
#         name = str(request.POST.get("name")).strip()
#         print(type(name))
#         res = None
#         data = []
#         if len(name) > 0:
#             qs = Patients.objects.filter(patientno__icontains=f"{name}")
#             for i in qs:
#                 item = {
#                     # "pk": i.patientid,
#                     "pin_no": i.patientno,
#                     "name": i.firstname,
#                     "surname": i.lastname,
#                 }

#                 print(f"{str(i.patientno)}000{str(i.totalvisits)}")
#                 data.append(item)
#             res = data
#         else:
#             res = "No Patient not found ........"

#             # return JsonResponse({"data": list(qs.values())})
#         # print(qs)
#         return JsonResponse({"data": res}, status=200)
#     return JsonResponse({"data": "Not found"}, status=400)


class PatientsClinicMasterList(generics.ListAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsClinicMasterSerializer
    # filter_class = PatientsClinicMasterFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["patientno",  "firstname", "lastname",]
    search_fields = ["patientno",  "firstname", "lastname",]
    
class PatientsClinicMasterDetail(generics.RetrieveAPIView): 
    queryset = Patients.objects.all()
    serializer_class = PatientsClinicMasterSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        try:
            patientno = self.kwargs.get("pk")
            clinic_master_patient = Patients.objects.filter(patientno=patientno)
            patient_in_physio_db = Patient.objects.filter(patientno=patientno)
        
            if patient_in_physio_db.exists():
                patient_has_admission = PhysioSessionAdmission.objects.filter(
                    patient__patientno=patientno
                ).filter(discharge=False)
                if patient_has_admission.exists():
                    #! more code  to be added here
                    response = {**request.data, 'patient_exists': True, 'admission_status': True}
                    return Response(response)
                response = {**dict(patient_in_physio_db.values()[0]), 'patient_exists': True , 'admission_status': False}
                print(response)
                return Response(response)
            clinic_master_patient_dat = dict(clinic_master_patient.values()[0])
            response = { **clinic_master_patient_dat, 'patient_exists': False}
            return Response(response)
        except Exception as e:
            # Handle exceptions here if needed
            print(e )
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class TherapyPatient(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientsTherapySerializer
    lookup_field = "pk"
    
    
    
    
    
    def post(self, request, *args, **kwargs):
        #if patient exits return json response patient already exits
        # else create patient
        # try:
            print(request.data)
            patientno = request.data["patientno"]
            existing_patient = Patient.objects.filter(patientno=patientno)
            if existing_patient.exists():
                existing_patient_admission = PhysioSessionAdmission.objects.filter(
                    patient__patientno=patientno
                ).filter(discharge=False)
                if existing_patient_admission.exists():
                    response = {**request.data, 'patient_exists': True, 'addmission_status': True}
                    return Response(response) # return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
                response = {**request.data, 'patient_exists': True, 'addmission_status': 
               False}
                return Response(response)
            # return self.create(request, *args, **kwargs)
            return super().post(request, *args, **kwargs)
        # except Exception as e:
        #     # Handle exceptions here if needed
        #     print(e)
        #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

   