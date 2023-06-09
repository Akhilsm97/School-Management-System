# Generated by Django 3.2.5 on 2022-08-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0011_xi_a_attendence_sheet_attendence_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vlll_B_attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=50)),
                ('date_of_attendance', models.CharField(max_length=50)),
                ('Attendence', models.CharField(max_length=50)),
                ('attendence_taken', models.CharField(max_length=50)),
                ('attendence_status', models.CharField(max_length=50)),
                ('attendance_stat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vlll_B_attendence_sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=50)),
                ('working_days', models.CharField(max_length=50)),
                ('Present', models.CharField(max_length=50)),
                ('Absent', models.CharField(max_length=50)),
                ('Half_day', models.CharField(max_length=50)),
                ('percent', models.CharField(max_length=100)),
                ('attendence_taken', models.CharField(max_length=50)),
            ],
        ),
    ]
