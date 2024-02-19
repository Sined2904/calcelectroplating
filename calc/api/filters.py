from django_filters import FilterSet, NumberFilter
from django_filters import rest_framework as filters
from .models import ElectrochemicalEquivalents
from django_filters.rest_framework import CharFilter, FilterSet, filters

class ElectrochemicalEquivalentsFilter(FilterSet):
    """Фильтр для материалов покрытия."""

    name = CharFilter(lookup_expr='startswith')

    class Meta:
        model = ElectrochemicalEquivalents
        fields = ('name',)
