# Generated by Django 2.2 on 2021-05-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.CharField(max_length=100),
        ),
    ]