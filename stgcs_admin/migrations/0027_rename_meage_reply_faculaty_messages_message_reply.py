# Generated by Django 3.2.5 on 2022-09-17 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stgcs_admin', '0026_faculaty_messages_meage_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculaty_messages',
            old_name='meage_reply',
            new_name='message_reply',
        ),
    ]
