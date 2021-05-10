from django.db import models


class Company_Detail(models.Model):
    comp_code = models.CharField(max_length=3)
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=50)
    company_location = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)


class System_data_head(models.Model):
    head_code = models.CharField(max_length=50)
    head_title = models.CharField(max_length=50)