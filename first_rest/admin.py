from django.contrib import admin
from first_rest.models import Student, College

# Register your models here.

admin.site.register([Student, College])