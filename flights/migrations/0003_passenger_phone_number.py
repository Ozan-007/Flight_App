# Generated by Django 4.0 on 2022-01-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
