from rest_framework import serializers
from django.db.models import Max, Min

from .models import Time, ElectrochemicalEquivalents, Height


class TimeSerializer(serializers.ModelSerializer):
    """Сериализатор расчета времени."""

    class Meta:
        model = Time
        fields = ['id', 'm', 'units_m', 'I', 'units_I', 'q', 'units_q',
                 'wt', 'S', 'units_S', 'j', 'units_j', 'p',
                 'units_p', 'h', 'units_h', 't']


class ElectrochemicalEquivalentsSerializer(serializers.ModelSerializer):
    """Сериализатор материалов покрытия."""

    class Meta:
        model = ElectrochemicalEquivalents
        fields = ['name', 'q', 'p']


class HeightSerializer(serializers.ModelSerializer):
    """Сериализатор расчета толщины."""

    class Meta:
        model = Height
        fields = ['id', 'm', 'units_m', 'I', 'units_I', 'q', 'units_q',
                 'wt', 'S', 'units_S', 'p',
                 'units_p', 't', 'units_t', 'v', 'units_v', 'h']