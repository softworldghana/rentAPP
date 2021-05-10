from django.db import models
from system_data.models import system_data

expense_CHOICES = list ((obj.data_name, obj.data_name) for obj in system_data.objects.filter(system_data_type='101'))


class expenditure(models.Model):
    expenditure_date = models.DateField()
    expenditure_purpose = models.CharField(max_length=50)
    expenditure_beneficiary = models.CharField(max_length=50)
    expenditure_amount = models.CharField(max_length=50)
    # expenditure_amount_return = models.DecimalField(max_digits=10, decimal_places=2)
    expenditure_group_no = models.CharField(max_length=50, choices=expense_CHOICES)

