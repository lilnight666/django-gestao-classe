# Generated by Django 4.1.7 on 2023-03-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0006_alter_respostaatividade_aprovacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="respostaatividade",
            name="arquivo",
            field=models.FileField(blank=True, upload_to="media/"),
        ),
    ]
