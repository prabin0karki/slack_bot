from django.contrib import admin
from django.contrib import admin
from leaveapp.models import Leave

# Register your models here.


class Leaveapp(admin.ModelAdmin):
    list_display = ("id", "title", "leave_type", "status", "user_name")


admin.site.register(Leave, Leaveapp)
