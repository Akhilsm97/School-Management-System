# Generated by Django 3.2.5 on 2022-09-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0022_add_portion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_portion',
            name='chapter',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='add_portion',
            name='classes',
            field=models.CharField(max_length=100),
        ),
    ]
