# Generated by Django 5.0.6 on 2024-05-14 20:24

import django.utils.timezone
import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("allocate", "0002_alter_allocate_student_to_room_room_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allocate_student_to_room",
            name="date",
            field=django_jalali.db.models.jDateTimeField(
                default=django.utils.timezone.now
            ),
        ),
    ]