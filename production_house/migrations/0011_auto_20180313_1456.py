# Generated by Django 2.0.2 on 2018-03-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_house', '0010_auto_20180302_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
    ]