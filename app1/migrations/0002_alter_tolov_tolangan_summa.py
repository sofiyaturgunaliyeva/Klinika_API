# Generated by Django 4.2 on 2023-07-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tolov',
            name='tolangan_summa',
            field=models.JSONField(default=[]),
        ),
    ]
