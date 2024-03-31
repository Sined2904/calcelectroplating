from rest_framework import serializers
from django.db.models import Max, Min

from .models import Time, ElectrochemicalEquivalents, Height


class TimeSerializer(serializers.ModelSerializer):
    """Сериализатор расчета времени."""

    class Meta:
        model = Time
        fields = ['m', 'units_m', 'I', 'units_I', 'q', 'units_q',
                 'wt', 'S', 'units_S', 'j', 'units_j', 'p',
                 'units_p', 'h', 'units_h', 't']


class TimeSerializerOutput(serializers.ModelSerializer):
    """Сериализатор расчета времени (возврат результата)."""

    t = serializers.SerializerMethodField()
    t_min = serializers.SerializerMethodField()
    t_hour = serializers.SerializerMethodField()

    class Meta:
        model = Time
        fields = ['t', 't_min', 't_hour']

    def get_t(self, object):
        return round(object.t%60)

    def get_t_min(self, object):
        return (object.t%3600)//60

    def get_t_hour(self, object):
        return round(object.t//3600)


class ElectrochemicalEquivalentsSerializer(serializers.ModelSerializer):
    """Сериализатор материалов покрытия."""

    class Meta:
        model = ElectrochemicalEquivalents
        fields = ['name', 'q', 'p']


class HeightSerializer(serializers.ModelSerializer):
    """Сериализатор расчета толщины."""

    class Meta:
        model = Height
        fields = ['m', 'units_m', 'I', 'units_I', 'q', 'units_q',
                 'wt', 'S', 'units_S', 'p',
                 'units_p', 't', 'units_t', 'v', 'units_v', 'h']


class HeigthSerializerOutput(serializers.ModelSerializer):
    """Сериализатор расчета толщины (возврат результата)."""
    
    h_m = serializers.SerializerMethodField()
    h_milli = serializers.SerializerMethodField()
    h_micro = serializers.SerializerMethodField()

    class Meta:
        model = Time
        fields = ['h_m', 'h_milli', 'h_micro']

    def get_h_m(self, object):
        return round(object.h, 6)

    def get_h_milli(self, object):
        return round(object.h*1000, 6)

    def get_h_micro(self, object):
        return round(object.h*1000000, 6)
