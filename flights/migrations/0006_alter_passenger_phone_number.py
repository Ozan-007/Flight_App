# Generated by Django 4.0 on 2022-01-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_passenger_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]