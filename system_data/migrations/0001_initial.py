# Generated by Django 2.2.4 on 2019-08-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='system_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_data_type', models.CharField(default='', max_length=10)),
                ('data_name', models.CharField(max_length=50)),
            ],
        ),
    ]
