# Generated by Django 4.2.3 on 2023-11-14 15:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="CertifyingInstitution",
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
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
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
                ("name", models.CharField(max_length=100)),
                (
                    "timestamp",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "certifying_institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.certifyinginstitution",
                    ),
                ),
                (
                    "profiles",
                    models.ManyToManyField(
                        related_name="certificates", to="projects.profile"
                    ),
                ),
            ],
        ),
    ]