# Generated by Django 5.0.6 on 2025-03-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_serviceprovider_availability_serviceprovider_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='experience',
            field=models.FloatField(blank=True, default=0.0, help_text='Experience in years', null=True),
        ),
    ]
