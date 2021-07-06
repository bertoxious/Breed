# Generated by Django 3.2 on 2021-07-01 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_alter_comment_cat'),
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogcomment',
            name='dog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dog_comments', to='homepage.dog'),
            preserve_default=False,
        ),
    ]