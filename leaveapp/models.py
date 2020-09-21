import requests
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


REQUEST_CHOICES = (
    ("pending", _("Pending")),
    ("accept", _("Accept")),
    ("reject", _("Reject")),
)

LEAVE_CHOICES = (
    ("first_half", _("First Half")),
    ("second_half", _("Second Half")),
    ("full_day", _("Full Day")),
)


class Leave(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(choices=REQUEST_CHOICES, default="pending", max_length=15)
    leave_type = models.CharField(
        choices=LEAVE_CHOICES, default="first_half", max_length=15
    )
    updated_at = models.DateField(null=True)
    user_name = models.CharField(max_length=50)
    leave_date = models.DateField(null=True)
    response_url = models.URLField(max_length=150, default="")

    class Meta:
        db_table = "leave"

    def __str__(self):
        return str(self.title)


@receiver(post_save, sender=Leave)
def update_status(sender, instance, created, **kwargs):
    if not created:
        if instance.status != "pending":
            message = "%s, %s %s" % (
                instance.user_name,
                "your application for leave have been",
                instance.status + "ed",
            )
            header = {"content-type": "application/json"}
            data_obj = {"text": message}
            requests.post(instance.response_url, headers=header, data=str(data_obj))


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(null=True)
    user_name = models.CharField(max_length=50)
    estimated_hour = models.FloatField()
    channel_id = models.CharField(max_length=150, default="")

    class Meta:
        db_table = "task"

    def __str__(self):
        return str(self.title)
