# Generated by Django 2.2.4 on 2019-08-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('occupation', models.CharField(default='N/A', max_length=50)),
                ('emergency_contact', models.CharField(default='N/A', max_length=50)),
            ],
        ),
    ]
