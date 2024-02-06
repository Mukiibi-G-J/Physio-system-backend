from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)

admin.site.register(Therapy)
admin.site.register(Diagnosis)
admin.site.register(Ward)
admin.site.register(Doctor)
