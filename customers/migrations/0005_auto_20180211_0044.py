# Generated by Django 2.0.2 on 2018-02-11 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20180207_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='old_mobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]