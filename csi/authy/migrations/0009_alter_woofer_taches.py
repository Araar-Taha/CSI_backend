# Generated by Django 5.1.7 on 2025-03-25 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0008_remove_woofer_participant_field'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woofer',
            name='taches',
            field=models.ManyToManyField(null=True, related_name='woofers', to='tasks.tache'),
        ),
    ]
