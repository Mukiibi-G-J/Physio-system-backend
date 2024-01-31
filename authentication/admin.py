from django.contrib import admin
from .models import Department
from .models import CustomUser
# Register your models here.
admin.site.register(Department)
admin.site.register(CustomUser)