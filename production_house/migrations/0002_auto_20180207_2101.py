# Generated by Django 2.0.2 on 2018-02-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_house', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='landline',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='video_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]