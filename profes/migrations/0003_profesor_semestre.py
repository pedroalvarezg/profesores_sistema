# Generated by Django 4.1 on 2023-04-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profes", "0002_alter_profesor_matricula"),
    ]

    operations = [
        migrations.AddField(
            model_name="profesor",
            name="semestre",
            field=models.IntegerField(default="0"),
            preserve_default=False,
        ),
    ]
