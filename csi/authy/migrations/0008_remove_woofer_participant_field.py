# Generated by Django 5.1.7 on 2025-03-25 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0007_woofer_datefinsejour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='woofer',
            name='participant_field',
        ),
    ]
