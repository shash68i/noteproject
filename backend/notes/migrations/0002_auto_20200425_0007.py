# Generated by Django 3.0.5 on 2020-04-25 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notetopic',
            name='topic',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
