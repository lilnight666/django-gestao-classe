# Generated by Django 4.1.7 on 2023-03-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0004_respostaatividade_aprovacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="respostaatividade",
            name="aprovacao",
            field=models.CharField(
                choices=[("A", "Aprovado"), ("R", "Reprovado")], max_length=1
            ),
        ),
        migrations.DeleteModel(
            name="Aprovacao",
        ),
    ]