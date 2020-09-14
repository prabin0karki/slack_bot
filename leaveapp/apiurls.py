from django.urls import path
from . import views

app_name = "leaveapp"
urlpatterns = [
    path("leave", views.leaveApply, name="leaveApply"),
    path("leaveinfo", views.leaveinfo, name="leaveinfo"),
]
