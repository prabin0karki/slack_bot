from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


REQUEST_CHOICES = (
    ("pending", _("Pending")),
    ("accepted", _("Accepted")),
    ("rejected", _("Rejected")),
)


class Leave(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateField()
    status = models.CharField(choices=REQUEST_CHOICES, default="pending", max_length=30)
    updated_at = models.DateField(null=True)
    user_name = models.CharField(max_length=50)

    class Meta:
        db_table = "leave"

    def __str__(self):
        return str(self.title)
