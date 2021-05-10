"""rentAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls'), name="dashboard"),
    path('agents/', include('agents.urls'), name="agents"),
    path('company/', include('company.urls'), name="company"),
    path('system_data/', include('system_data.urls'), name="system_data"),
    path('properties/', include('properties.urls'), name="properties"),
    path('rent/', include('rent.urls'), name="rent"),
    path('tenant_details/', include('tenant_details.urls'), name="tenant_details"),
    path('expenses/', include('expenditure.urls'), name="expenditure"),
]