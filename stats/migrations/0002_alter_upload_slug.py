# Generated by Django 4.1.1 on 2022-09-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='slug',
            field=models.SlugField(max_length=10, unique=True),
        ),
    ]
