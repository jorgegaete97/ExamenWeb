from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(UserAdmin):
    fieldsets = (
        ('Credenciales', {
            'fields': ('username','password')}),
        ('Información personal', {
            "fields": ('email','first_name','last_name','direccion',)}),
        ('Permisos', {
            "fields": ('is_active','is_staff',)}),

    )

admin.site.register(User,UserAdmin)