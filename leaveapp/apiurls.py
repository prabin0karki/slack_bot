from django.urls import path
from . import views

app_name = "leaveapp"
urlpatterns = [
    path("leave", views.leaveApply, name="leaveApply"),
    path("leaveinfo", views.leaveinfo, name="leaveinfo"),
    # path("leaveinfo", views.Events1.as_view()),
    # path("leave", views.Events.as_view()),
]
