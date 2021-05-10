from django.db import models
from company.models import System_data_head

CHOICES = list ((obj.head_code, obj.head_title) for obj in System_data_head.objects.all())


class system_data(models.Model):
    system_data_type = models.CharField(max_length=10, choices=CHOICES, default='')
    data_name = models.CharField(max_length=50)

