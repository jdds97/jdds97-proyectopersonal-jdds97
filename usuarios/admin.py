"""
Sitio de administración
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Staff, Admin, Instructor, Cliente


admin.site.register(Admin, UserAdmin)
admin.site.register(Staff, UserAdmin)
admin.site.register(Instructor)
admin.site.register(Cliente)


# Register your models here.
