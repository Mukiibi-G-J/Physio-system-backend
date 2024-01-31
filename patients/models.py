from django.db import models
from authentication.models import CustomUser


class Patient(models.Model):
    patient_no = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField(auto_now_add=False)
    phone_number = models.CharField(max_length=10)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    @property
    def get_full_name(self):
        return self.lastname + " " + self.firstname
    # creating a function to get patient current physiso session left

    @property
    def get_current_session(self):
        sessions = self.patient_physio_admission.filter(discharge=False)
        if sessions.exists():
            #  Check if the last session has the attribute 'quantity_of_session_left'
            last_session = sessions[0].physio_admission_no.last()

            if last_session and hasattr(last_session, 'quantity_of_session_left'):
                quantity_of_session_left = last_session.quantity_of_session_left
            else:
                # If 'quantity_of_session_left' is not present, fallback to 'quantity_of_sessions'
                quantity_of_session_left = sessions[0].quantity_of_sessions

            return str(quantity_of_session_left)

        else:
            # Handle the case when there are no sessions left
            return "No sessions available"
            

    def __str__(self):
        return self.get_full_name


class Therapy(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brief_description = models.TextField(
        null=True, blank=True, default="No description"
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    brief_description = models.TextField(
        null=True, blank=True, default="No description"
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Speciality(models.Model):
    speciality = models.CharField(
        max_length=255, null=True, blank=True
    )
    def __str__(self):
        return self.speciality
class Doctor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    specialist = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Ward(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brief_description = models.TextField(
        null=True, blank=True, default="No description"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
