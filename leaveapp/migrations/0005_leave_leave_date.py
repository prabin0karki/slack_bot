# Generated by Django 3.1.1 on 2020-09-18 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaveapp", "0004_auto_20200914_1451"),
    ]

    operations = [
        migrations.AddField(
            model_name="leave",
            name="leave_date",
            field=models.DateField(null=True),
        ),
    ]