# Generated by Django 5.1.7 on 2025-03-24 02:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_participant_woofer'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='participant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authy.participant'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='woofer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authy.woofer'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='participant_instance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='woofer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='woofer_instance', to=settings.AUTH_USER_MODEL),
        ),
    ]
