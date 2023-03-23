# Generated by Django 4.1.7 on 2023-03-06 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0002_aprovacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aprovacao",
            name="resposta",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="aprovacoes",
                to="classes.respostaatividade",
            ),
        ),
    ]
