# Generated by Django 3.2.5 on 2022-08-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0010_xi_a_attendence_sheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='xi_a_attendence_sheet',
            name='attendence_taken',
            field=models.CharField(default='ASWATHI  KUMARI S', max_length=50),
            preserve_default=False,
        ),
    ]
