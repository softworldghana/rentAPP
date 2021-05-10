from django.contrib import admin
from . models import Property_List


class prop_list(admin.ModelAdmin):
    list_display = ('property_name', 'location', 'location', 'contact_person', 'agent_name', 'property_completion_date', 'cost_of_const', 'no_of_rooms', 'room_types')


admin.site.register(Property_List, prop_list)