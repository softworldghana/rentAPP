from django.contrib import admin
from . models import agents


class agent_list(admin.ModelAdmin):
    list_display = ('agent_name', 'location', 'telephone', 'date_added', 'user')


admin.site.register(agents, agent_list)
