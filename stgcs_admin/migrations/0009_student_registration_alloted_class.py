# Generated by Django 3.2.5 on 2022-08-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0008_xi_a_attendence_attendance_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_registration',
            name='alloted_class',
            field=models.CharField(default='-', max_length=20),
            preserve_default=False,
        ),
    ]
