# Generated by Django 3.2 on 2021-06-28 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_alter_comment_cat'),
        ('cats', '0003_alter_commentoncat_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentoncat',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cat_comments', to='homepage.cat'),
            preserve_default=False,
        ),
    ]
