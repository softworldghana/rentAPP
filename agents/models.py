from django.conf import settings
from django.db import models


class agents(models.Model):
    agent_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.agent_name