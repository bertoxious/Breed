# Generated by Django 3.2 on 2021-06-15 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cattle',
            name='breed_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]