# Generated by Django 4.1.6 on 2023-02-17 18:27

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('EasyGo', '0003_alter_staff_staffname_alter_staff_staffphonenumber'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='staff',
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]