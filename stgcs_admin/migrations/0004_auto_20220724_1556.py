# Generated by Django 3.2.5 on 2022-07-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0003_approved_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers_registration',
            name='per_comp',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers_registration',
            name='teac_ach',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
    ]