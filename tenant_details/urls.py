from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenant_details)
]