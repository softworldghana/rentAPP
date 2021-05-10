from django.db import models
from properties.models import Property_List
from system_data.models import system_data
from tenant_details.models import Tenant_details

""" CHOICES = list ((obj.property_name, obj.property_name) for obj in Property_List.objects.all())
ROOM_CHOICES = list ((obj.data_name, obj.data_name) for obj in system_data.objects.filter(system_data_type='103'))
tenant_CHOICES = list ((obj.tenant_name, obj.tenant_name) for obj in Tenant_details.objects.all())
 """


class Rent(models.Model):
    """ tenant_name = models.CharField(max_length=50, choices=tenant_CHOICES)
    property_name = models.CharField(max_length=50, choices=CHOICES)
    room_types = models.CharField(max_length=50, choices=ROOM_CHOICES) """
    duration_from = models.DateField()
    duration_to = models.DateField()
    rent_per_month = models.FloatField(default='0')
    total_rent = models.FloatField(default='0')
    deposit_amt = models.FloatField(default='0')
