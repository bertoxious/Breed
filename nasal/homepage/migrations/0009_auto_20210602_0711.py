# Generated by Django 3.2 on 2021-06-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_remove_dog_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='appearance',
            field=models.CharField(default='Sex', max_length=10000),
        ),
        migrations.AlterField(
            model_name='cat',
            name='temperament',
            field=models.CharField(max_length=10000),
        ),
    ]
