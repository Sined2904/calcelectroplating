from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView

from .views import TimeViewSet, ElectrochemicalEquivalentsViewSet, HeightViewSet, WeightViewSet, CurrentDensityViewSet, AmperageViewSet

app_name = 'api'

router = DefaultRouter()

router.register('time', TimeViewSet, basename='time')
router.register('el_eqts', ElectrochemicalEquivalentsViewSet, basename='el_eqts')
router.register('height', HeightViewSet, basename='height')
router.register('weight', WeightViewSet, basename='weight')
router.register('currentdensity', CurrentDensityViewSet, basename='currentdensity')
router.register('amperage', AmperageViewSet, basename='currentdensity')


urlpatterns = [
    path('', include(router.urls)),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(),
         name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema2'),
         name='redoc'),
]