# Generated by Django 4.1.7 on 2023-03-21 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0010_atividade_turma"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="atividade",
            name="turma",
        ),
    ]