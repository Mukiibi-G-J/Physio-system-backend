from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name



class CustomManager(BaseUserManager):
    def create_user(self, email, username, first_name,last_name,phone_number, password=None,**extra_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name ,last_name=last_name, phone_number=phone_number, **extra_fields)
        
        user.set_password(password)                
            
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, username, first_name,last_name, phone_number,password=None, **extra_fields, ):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must be assigned to is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be assigned to is_superuser=True')
        user = self.create_user(email, username, first_name, last_name, phone_number, password, **extra_fields)
        # user.is_staff = True
        # user.is_superuser = True
        user.save(using=self._db)
        return user
 
    
   
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(_('email address'), unique=True)
        username = models.CharField(max_length=255, unique=True)
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        phone_number = models.CharField(max_length=10)
        start_date = models.DateField(default=timezone.now)
        otp = models.CharField(max_length=255, blank=True)
        is_verified = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        therapist = models.BooleanField(default=False)
        date_of_birth = models.DateField(null=True, blank=True)
        profile_image = models.ImageField(
        upload_to="images/", null=True, blank=True, default="path/to/upload/directory/")
        department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)
        
        objects = CustomManager()
        
        
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username', 'first_name', 'last_name', "phone_number"]
        
        def __str__(self):
            return self.username
    
        def save(self, *args, **kwargs):
            # Check if the password is provided and not already hashed
            if self.password and not self.password.startswith(
                ("pbkdf2_sha256$", "bcrypt", "argon2")
            ):
                self.password = make_password(self.password)
            super().save(*args, **kwargs)

        @property
        def full_name(self):
            return self.first_name + " " + self.last_name
                
        

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)