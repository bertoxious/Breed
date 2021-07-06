# Generated by Django 3.2 on 2021-07-01 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_alter_comment_cat'),
        ('cats', '0005_alter_commentoncat_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentoncat',
            name='cat',
            field=models.ForeignKey(blank=True, db_column='cat', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_comments', to='homepage.cat'),
        ),
    ]
