# Generated by Django 3.2 on 2021-04-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=200)),
                ('country_origin', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('lifespan', models.CharField(max_length=100)),
                ('brief', models.CharField(max_length=1000)),
                ('images', models.ImageField(upload_to='')),
                ('comment_id', models.IntegerField(unique=True)),
                ('popularity', models.IntegerField()),
                ('danger', models.IntegerField()),
                ('temperament', models.CharField(max_length=200)),
            ],
        ),
    ]