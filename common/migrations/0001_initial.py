# Generated by Django 4.0.4 on 2022-06-14 13:38

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientUserPlatform",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=10, unique=True)),
                ("code", models.CharField(max_length=4, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomerProxy",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("customer_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("timezone", models.CharField(default="Asia/Qatar", max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PackageProxy",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("package_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("no_of_users", models.IntegerField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Permission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=10, unique=True)),
                ("code", models.CharField(max_length=4, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserPreferenceProxy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("guid", models.CharField(max_length=100, unique=True)),
                ("is_notification_enabled", models.BooleanField(default=True)),
                ("is_email_enabled", models.BooleanField(default=True)),
                ("is_sms_enabled", models.BooleanField(default=True)),
                ("platform_notification_duration", models.IntegerField(default=0)),
                ("asset_tamper_duration", models.IntegerField(default=0)),
                ("low_battery_duration", models.IntegerField(default=0)),
                ("env_temp_duration", models.IntegerField(default=4)),
                ("env_humidity_duration", models.IntegerField(default=4)),
                ("env_pressure_duration", models.IntegerField(default=4)),
                ("geofence_entry_exit_duration", models.IntegerField(default=12)),
                ("asset_allocation_duration", models.IntegerField(default=12)),
                ("asset_prolong_alloc_duration", models.IntegerField(default=24)),
                ("asset_loss_theft_duration", models.IntegerField(default=0)),
                ("idling_duration", models.IntegerField(default=0)),
                ("page_size", models.IntegerField(blank=True, default=10, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserProxy",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("guid", models.UUIDField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("username", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "password",
                    models.CharField(
                        blank=True, default=None, max_length=128, null=True
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("department", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("1", "Super Admin"),
                            ("2", "Admin"),
                            ("3", "Consumer"),
                            ("4", "Driver"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("data_joined", models.DateTimeField(null=True)),
                (
                    "work_location",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "internal_role",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.customerproxy",
                    ),
                ),
                (
                    "permissions",
                    models.ManyToManyField(blank=True, to="common.permission"),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserLoginProxy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("fcm_token", models.CharField(blank=True, max_length=500, null=True)),
                ("is_valid", models.BooleanField(blank=True, default=True, null=True)),
                ("login_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.customerproxy",
                    ),
                ),
                (
                    "platform",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.clientuserplatform",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.userproxy",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserBlacklistedToken",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("guid", models.CharField(blank=True, max_length=50, null=True)),
                ("token", models.TextField()),
                (
                    "platform",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.clientuserplatform",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomerPackageAllocationProxy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Active"),
                            ("2", "Inactive"),
                            ("3", "Deleted"),
                            ("4", "Blocked"),
                        ],
                        default="1",
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.customerproxy",
                    ),
                ),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.packageproxy",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]