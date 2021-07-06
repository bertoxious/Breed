# Generated by Django 3.2 on 2021-05-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='monte@carlo.com', max_length=254),
        ),
    ]