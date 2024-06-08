from rest_framework import serializers
from django.db.models import Max, Min

from .models import Time, ElectrochemicalEquivalents, Height, Weight, CurrentDensity, Amperage


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

    class Meta:
        model = Time
        fields = ['h']


class WeightSerializer(serializers.ModelSerializer):
    """Сериализатор расчета массы."""

    class Meta:
        model = Weight
        fields = ['h', 'units_h', 'I', 'units_I', 'q', 'units_q',
                 'wt', 'S', 'units_S', 'p',
                 'units_p', 't', 'units_t']


class WeigthSerializerOutput(serializers.ModelSerializer):
    """Сериализатор расчета массы (возврат результата)."""

    class Meta:
        model = Weight
        fields = ['m']


class CurrentDensitySerializer(serializers.ModelSerializer):
    """Сериализатор расчета плотности тока."""

    class Meta:
        model = CurrentDensity
        fields = ['I', 'units_I', 'S1', 'units_S1', 'S2', 'units_S2', 
                  'S3', 'units_S3', 'S4', 'units_S4', 'S5', 'units_S5',
                  'S6', 'units_S6', 'S7', 'units_S7', 'S8', 'units_S8',
                  'S9', 'units_S9', 'S10', 'units_S10', 'S11', 'units_S11', 
                  'S12', 'units_S12', 'S13', 'units_S13', 'S14', 'units_S14',
                  'S15', 'units_S15', 'S16', 'units_S16', 'S17', 'units_S17',
                  'S18', 'units_S18', 'S19', 'units_S19', 'S20', 'units_S20']


class CurrentDensitySerializerOutput(serializers.ModelSerializer):
    """Сериализатор расчета плотности тока (возврат результата)."""

    class Meta:
        model = CurrentDensity
        fields = ['j']


class AmperageSerializer(serializers.ModelSerializer):
    """Сериализатор расчета силы тока."""

    class Meta:
        model = Amperage
        fields = ['j', 'units_j', 'S1', 'units_S1', 'S2', 'units_S2', 
                  'S3', 'units_S3', 'S4', 'units_S4', 'S5', 'units_S5',
                  'S6', 'units_S6', 'S7', 'units_S7', 'S8', 'units_S8',
                  'S9', 'units_S9', 'S10', 'units_S10', 'S11', 'units_S11', 
                  'S12', 'units_S12', 'S13', 'units_S13', 'S14', 'units_S14',
                  'S15', 'units_S15', 'S16', 'units_S16', 'S17', 'units_S17',
                  'S18', 'units_S18', 'S19', 'units_S19', 'S20', 'units_S20']


class AmperageSerializerOutput(serializers.ModelSerializer):
    """Сериализатор расчета плотности тока (возврат результата)."""

    class Meta:
        model = CurrentDensity
        fields = ['I']