# Generated by Django 3.0.7 on 2020-06-14 23:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0015_auto_20200614_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
