# Generated by Django 2.0.2 on 2018-03-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20180313_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_photo'),
        ),
    ]