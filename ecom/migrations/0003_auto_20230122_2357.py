# Generated by Django 3.0.5 on 2023-01-22 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_auto_20230122_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='nom',
            new_name='name',
        ),
    ]