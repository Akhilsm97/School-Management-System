# Generated by Django 3.2.5 on 2022-08-08 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0005_xi_a_attendence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xi_a_attendence',
            old_name='date',
            new_name='date_of_attendance',
        ),
    ]
