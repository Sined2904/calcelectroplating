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
    list_display = ['id', 'I', 'units_I', 'S1', 'units_S1', 'S2', 'units_S2', 
                  'S3', 'units_S3', 'S4', 'units_S4', 'S5', 'units_S5',
                  'S6', 'units_S6', 'S7', 'units_S7', 'S8', 'units_S8',
                  'S9', 'units_S9', 'S10', 'units_S10', 'S11', 'units_S11', 
                  'S12', 'units_S12', 'S13', 'units_S13', 'S14', 'units_S14',
                  'S15', 'units_S15', 'S16', 'units_S16', 'S17', 'units_S17',
                  'S18', 'units_S18', 'S19', 'units_S19', 'S20', 'units_S20', 'j']
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
