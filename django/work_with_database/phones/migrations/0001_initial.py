# Generated by Django 5.0.6 on 2024-06-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("image", models.ImageField(max_length=255, upload_to="")),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("release_date", models.DateField(max_length=10)),
                ("lte_exists", models.BooleanField()),
                ("slug", models.SlugField(max_length=25)),
            ],
        ),
    ]
