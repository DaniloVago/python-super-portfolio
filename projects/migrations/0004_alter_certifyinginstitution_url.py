# Generated by Django 4.2.3 on 2023-11-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certifyinginstitution",
            name="url",
            field=models.URLField(max_length=500),
        ),
    ]
