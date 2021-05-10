from django.contrib import admin
from . models import system_data


class system_list(admin.ModelAdmin):
    list_display = ('system_data_type', 'data_name')


admin.site.register(system_data, system_list)

