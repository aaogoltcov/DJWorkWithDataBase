# Generated by Django 3.0.7 on 2020-06-14 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_auto_20200614_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(),
        ),
    ]