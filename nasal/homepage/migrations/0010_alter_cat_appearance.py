# Generated by Django 3.2 on 2021-06-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20210602_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='appearance',
            field=models.CharField(max_length=10000),
        ),
    ]