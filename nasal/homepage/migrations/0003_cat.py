# Generated by Django 3.2 on 2021-04-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_rename_dogs_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=200)),
                ('country_origin', models.CharField(max_length=200)),
                ('breed_type', models.CharField(max_length=100)),
                ('body_type', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=1000)),
                ('images', models.ImageField(upload_to='')),
                ('comment_id', models.IntegerField(unique=True)),
                ('popularity', models.IntegerField()),
                ('danger', models.IntegerField()),
                ('coat_pattern', models.CharField(max_length=200)),
            ],
        ),
    ]
