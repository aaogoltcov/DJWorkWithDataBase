# Generated by Django 3.0.7 on 2020-06-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20200614_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]