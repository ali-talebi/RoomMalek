# Generated by Django 5.0.6 on 2024-05-14 20:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Student", "0003_alter_student_information_phone"),
        ("allocate", "0001_initial"),
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allocate_student_to_room",
            name="room",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="room_allocated",
                to="home.room",
                verbose_name="اتاق",
            ),
        ),
        migrations.AlterField(
            model_name="allocate_student_to_room",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="student_allocated",
                to="Student.student_information",
                unique=True,
                verbose_name="دانشجو",
            ),
        ),
    ]