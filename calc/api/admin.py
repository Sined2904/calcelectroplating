from django.contrib import admin

from .models import Time, ElectrochemicalEquivalents, Height, Weight, CurrentDensity, Amperage


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


class HeightAdmin(admin.ModelAdmin):
    list_display = ['id', 'm', 'units_m', 'I', 'units_I', 'q', 'units_q',
                    'wt', 'S', 'units_S', 'p', 'units_p', 'h', 't', 'units_t',
                    'v', 'units_v']
    empty_value_display = '-пусто-'
    ordering = ['id',]


class WeightAdmin(admin.ModelAdmin):
    list_display = ['id', 'm', 'I', 'units_I', 'q', 'units_q',
                    'wt', 'S', 'units_S', 'j', 'units_j', 'p',
                    'units_p', 'h', 'units_h', 't', 'units_t']
    empty_value_display = '-пусто-'
    ordering = ['id',]


class CurrentDensityAdmin(admin.ModelAdmin):
    list_display = ['id', 'S', 'j', 'I']
    empty_value_display = '-пусто-'
    ordering = ['id',]


class AmperageAdmin(admin.ModelAdmin):
    list_display = ['id', 'S', 'j', 'I']
    empty_value_display = '-пусто-'
    ordering = ['id',]


admin.site.register(Time, TimeAdmin)
admin.site.register(ElectrochemicalEquivalents, ElectrochemicalEquivalentsAdmin)
admin.site.register(Height, HeightAdmin)
admin.site.register(Weight, WeightAdmin)
admin.site.register(CurrentDensity, CurrentDensityAdmin)
admin.site.register(Amperage, AmperageAdmin)
