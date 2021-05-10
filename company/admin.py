from django.contrib import admin
from . models import Company_Detail


class comp_list(admin.ModelAdmin):
    list_display = ('comp_code', 'company_name', 'company_address', 'company_location', 'telephone', 'email', 'website')


admin.site.register(Company_Detail, comp_list)