# Generated by Django 3.1 on 2020-08-09 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Id',
            new_name='idno',
        ),
    ]