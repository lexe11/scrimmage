# Generated by Django 4.1.1 on 2022-09-28 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_alter_upload_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='slug',
        ),
    ]
