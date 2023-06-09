# Generated by Django 4.0.4 on 2022-06-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0005_contractproxy_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="contractproxy",
            name="contract_latitude",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="contractproxy",
            name="contract_longitude",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="contractproxy",
            name="contract_status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
