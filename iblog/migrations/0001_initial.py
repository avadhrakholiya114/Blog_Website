# Generated by Django 4.2.7 on 2023-12-02 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categpry",
            fields=[
                ("cat_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("desc", models.TextField()),
                ("url", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="category/")),
                ("add_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("url", models.CharField(max_length=100)),
                ("img", models.ImageField(upload_to="post/")),
                (
                    "caatagory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="iblog.categpry"
                    ),
                ),
            ],
        ),
    ]
