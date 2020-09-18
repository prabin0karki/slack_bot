# Generated by Django 3.1.1 on 2020-09-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaveapp", "0005_leave_leave_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="leave",
            name="channel_id",
            field=models.CharField(default="", max_length=150),
        ),
        migrations.AlterField(
            model_name="leave",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accept", "Accept"),
                    ("reject", "Reject"),
                ],
                default="pending",
                max_length=15,
            ),
        ),
    ]
