# Generated by Django 3.2.5 on 2022-08-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0009_student_registration_alloted_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='XI_A_attendence_sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=50)),
                ('working_days', models.CharField(max_length=50)),
                ('Present', models.CharField(max_length=50)),
                ('Absent', models.CharField(max_length=50)),
                ('Half_day', models.CharField(max_length=50)),
                ('percent', models.CharField(max_length=100)),
            ],
        ),
    ]