from django.db import models
from agents.models import agents
from system_data.models import system_data
from multiselectfield import MultiSelectField

CHOICES = list ((obj.agent_name, obj.agent_name) for obj in agents.objects.all())
ROOM_CHOICES = list ((obj.data_name, obj.data_name) for obj in system_data.objects.filter(system_data_type='103'))


class Property_List(models.Model):
    property_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    contact_person_no = models.CharField(max_length=50)
    agent_name = models.CharField(max_length=50, choices=CHOICES, default='')
    care_taker = models.CharField(max_length=50, default='N/A')
    property_completion_date = models.DateField()
    cost_of_const = models.FloatField(default='0.00')
    no_of_rooms = models.IntegerField(default='1')
    room_types = MultiSelectField(choices=ROOM_CHOICES)