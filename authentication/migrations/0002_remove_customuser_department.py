# Generated by Django 5.0.1 on 2024-01-26 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
    ]
