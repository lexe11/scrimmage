# Generated by Django 4.1.1 on 2022-09-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('file', models.FileField(upload_to='uploads')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded_on'],
            },
        ),
    ]