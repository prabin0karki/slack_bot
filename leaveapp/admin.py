from django.contrib import admin
from leaveapp.models import Leave, Task

# Register your models here.


class Leaveapp(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "leave_type",
        "status",
        "user_name",
        "leave_date",
        "created_at",
    )


admin.site.register(Leave, Leaveapp)


class Taskapp(admin.ModelAdmin):
    list_display = ("id", "title", "estimated_hour", "user_name", "created_at")


admin.site.register(Task, Taskapp)
