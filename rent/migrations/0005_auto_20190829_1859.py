# Generated by Django 2.2.4 on 2019-08-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20190828_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='duration_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rent',
            name='duration_to',
            field=models.DateTimeField(),
        ),
    ]
