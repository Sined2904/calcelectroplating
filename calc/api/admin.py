from django.contrib import admin

from .models import Time, ElectrochemicalEquivalents


class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'm', 'units_m', 'I', 'units_I', 'q', 'units_q',
                    'wt', 'S', 'units_S', 'j', 'units_j', 'p',
                    'units_p', 'h', 'units_h']
    empty_value_display = '-пусто-'


class ElectrochemicalEquivalentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'q', 'p']
    empty_value_display = '-пусто-'
    search_fields = ('name', 'q')
    ordering = ['name', 'q']

admin.site.register(Time, TimeAdmin)
admin.site.register(ElectrochemicalEquivalents, ElectrochemicalEquivalentsAdmin)
