# Generated by Django 4.0.5 on 2022-12-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
