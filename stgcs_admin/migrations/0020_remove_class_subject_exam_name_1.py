# Generated by Django 3.2.5 on 2022-08-26 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0019_class_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_subject',
            name='exam_name_1',
        ),
    ]
