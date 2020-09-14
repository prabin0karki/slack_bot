from django.urls import path
from . import views

app_name = "leaveapp"
urlpatterns = [path("hello", views.leaveApply, name="leaveApply")]
