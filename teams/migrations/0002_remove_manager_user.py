# Generated by Django 2.2.4 on 2019-08-29 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
    ]
