# Generated by Django 2.2.4 on 2019-09-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenditure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='expenditure_amount_return',
        ),
        migrations.AlterField(
            model_name='expenditure',
            name='expenditure_group_no',
            field=models.CharField(choices=[('Building Maintenance', 'Building Maintenance')], max_length=50),
        ),
    ]