from django.db import models

sex_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

m_choices = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
)


class Tenant_details(models.Model):
    tenant_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=sex_choices)
    occupation = models.CharField(max_length=50, default='N/A')
    emergency_contact = models.CharField(max_length=50, default='N/A')

