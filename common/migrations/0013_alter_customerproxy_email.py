# Generated by Django 3.2.7 on 2022-07-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0012_vehicleproxy_device_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerproxy",
            name="email",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]