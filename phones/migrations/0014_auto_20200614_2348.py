# Generated by Django 3.0.7 on 2020-06-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0013_auto_20200614_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(verbose_name=models.TextField()),
        ),
    ]
