from django.contrib import admin
from . models import Tenant_details


class tenant_list(admin.ModelAdmin):
    list_display = ('tenant_name', 'contact_no', 'gender', 'occupation', 'emergency_contact')


admin.site.register(Tenant_details, tenant_list)
