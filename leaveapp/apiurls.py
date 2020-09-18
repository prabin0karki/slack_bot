from django.urls import path
from . import views

app_name = "leaveapp"
urlpatterns = [
    path("leaveinfo", views.LeaveEventInfo.as_view()),
    path("leave", views.LeaveEvent.as_view()),
    path("task", views.TaskEvent.as_view()),
    # path("leave", views.leaveApply, name="leaveApply"),
]
