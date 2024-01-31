import datetime

from django.db import models
from authentication.models import CustomUser
from patients.models import Patient, Ward, Doctor, Diagnosis, Therapy
from authentication.models import Department


class PhysioSessionAdmission(models.Model):
    admission_no = models.CharField(max_length=255, unique=True)
    therapist = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patient_physio_admission"
    )
    date_of_visit = models.DateField(auto_now_add=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.CASCADE, related_name="diagnosis_physio_admission"
    )
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    discharge = models.BooleanField(default=False)
    discharge_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    more_notes = models.TextField()
    patient_type = models.CharField(max_length=255)
    clinic_master_admission_no = models.CharField(max_length=255, blank=True, null=True)
    quantity_of_sessions = models.PositiveIntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def save(self, patient_no=None, *args, **kwargs):
        if not self.pk:
            print("patient_no", patient_no)
            print("self.pk", self.pk)
            print("args", args)
            print("self", self.patient)
            print("kwargs", kwargs)

            last_admission = PhysioSessionAdmission.objects.filter(
                discharge=True
            ).filter(patient__patient_no=self.patient.patient_no)
            # Check if the last admission exists and is not closed
            # if last_admission and not last_admission.discharge:
            #     # If the last admission is not closed, raise an exception or handle it as needed
            #     raise ValueError(
            #         "Cannot open a new admission while the previous one is still open."
            #     )
            print("last_admission", last_admission)
            # last_admission = PhysioSessionAdmission.objects.order_by("-id").first()
            if len(last_admission) > 0:
                last_admission = last_admission.last()
                admission_parts = last_admission.admission_no.split("-")
                last_id = int(last_admission.admission_no.split("-")[-1][3:])

                print(last_id)
                self.admission_no = (
                    f"{self.patient.patient_no}-PHA{str(last_id + 1).zfill(4)}"
                )
                print(self.admission_no)

            else:
                self.admission_no = f"{self.patient.patient_no}-PHA0001"
        # super().save(*args, **kwargs)
        return super().save(*args, **kwargs)


class PhysioSession(models.Model):
    physiosession_no = models.CharField(max_length=255)
    admission_no = models.ForeignKey(
        PhysioSessionAdmission, models.CASCADE, related_name="physio_admission_no"
    )
    therapy = models.ManyToManyField(Therapy, default="Old Therapy")
    more_notes = models.TextField()
    therapist = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    quantity_of_session_left = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, patient_no=None, *args, **kwargs):
        # i want to prvent user from opening a new admission if old is not closed
        # user can only have one admission at a time

        if not self.pk:
            last_admission = (
                PhysioSessionAdmission.objects.filter(patient__patient_no=patient_no)
                .order_by("-id")
                .first()
            )

            last_physioSession = (
                PhysioSession.objects.filter(admission_no=last_admission)
                .order_by("-id")
                .first()
            )

            if last_physioSession:
                last_id = int(last_physioSession.physiosession_no.split("-")[-1][2:])
                self.physiosession_no = f"{patient_no}-PH{str(last_id + 1).zfill(4)}"
                self.admission_no = last_admission
                print(self.admission_no)
            else:
                self.physiosession_no = f"{patient_no}-PH0001"
                self.admission_no = last_admission

        super().save(*args, **kwargs)


class Receipt(models.Model):
    physiosessionadmission = models.ForeignKey(
        PhysioSessionAdmission,
        on_delete=models.CASCADE,
        related_name="receipt_physiosessionadmission",
    )
    receipt_number = models.CharField(max_length=50, unique=True)
    quantity_of_session = models.PositiveIntegerField()
    visit_no = models.CharField(max_length=255)
    payment_date = models.DateField()
    # add other fields as needed


class Invoice(models.Model):
    physiosessionadmission = models.ForeignKey(
        PhysioSessionAdmission,
        on_delete=models.CASCADE,
        related_name="invoice_physiosessionadmission",
    )

    invoice_number = models.CharField(max_length=50)
    quantity_of_session = models.PositiveIntegerField()
    invoice_date = models.DateField()
    visit_no = models.CharField(max_length=255)


class TotalSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_quantity_of_session = models.PositiveIntegerField()



class RequestForInpatient(models.Model):
    patient_no = models.CharField(max_length=255)
    patient_full_name = models.CharField(max_length=255)
    request_body = models.TextField()
    request_date = models.DateField(auto_now_add=True)
    request_status = models.BooleanField(default=False)
    request_to_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    