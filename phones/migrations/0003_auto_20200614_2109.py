# Generated by Django 3.0.7 on 2020-06-14 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20200614_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.TextField(),
        ),
    ]
