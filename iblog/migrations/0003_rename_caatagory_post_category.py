# Generated by Django 4.2.7 on 2023-12-02 20:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("iblog", "0002_rename_categpry_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="caatagory",
            new_name="Category",
        ),
    ]
