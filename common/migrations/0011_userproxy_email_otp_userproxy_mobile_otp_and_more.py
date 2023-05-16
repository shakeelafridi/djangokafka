# Generated by Django 4.0.4 on 2022-07-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0010_delete_contractproxy"),
    ]

    operations = [
        migrations.AddField(
            model_name="userproxy",
            name="email_otp",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name="userproxy",
            name="mobile_otp",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name="userproxy",
            name="otp_expiry",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userproxy",
            name="reset_token",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]