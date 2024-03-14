from django.shortcuts import render
from .models import Time, ElectrochemicalEquivalents, Height
from rest_framework.response import Response
from .serializers import TimeSerializer, ElectrochemicalEquivalentsSerializer, HeightSerializer
from .filters import ElectrochemicalEquivalentsFilter
from rest_framework import viewsets, filters, status
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend


def converter_m(m, units_m):
    """Конвертер из грамм и милиграмм в кг."""
    if m != None:
        if units_m == 'г':
            m = m/1000
        if units_m == 'мг':
            m = m/1000000
    return m


def converter_I(I, units_I):
    """Конвертер силы тока из мА в А."""

    if units_I != 'А' and I is not None:
        I = I/1000
    return I


def converter_S(S, units_S):
    """Конвертер площади в м2."""

    if S != None:
        if units_S == 'дм2':
            S = S/100
        if units_S == 'см2':
            S = S/10000
        if units_S == 'мм2':
            S = S/1000000
    return S


def converter_j(j, units_j):
    """Конвертер плотности тока."""

    if j != None:
        if units_j == 'А/дм2':
            j = j*100
        if units_j == 'мА/см2':
            j = j*10
    return j


def converter_p(p, units_p):
    """Конвертер плотности покрытия."""

    if p != None:
        if units_p == 'гр/см3':
            p = p*1000
    return p


def converter_h(h, units_h):
    """Конвертер толщины покрытия из мм и мкм в м."""

    if h != None:
        if units_h == 'мм':
            h = h/1000
        if units_h == 'мкм':
            h = h/1000000
    return h


def converter_q(q, units_q):
    """Конвертер электрохимического эквивалента в кг/Кл."""

    if q != None:
        if units_q == 'мг/Кл':
            q = q/1000000
        if units_q == 'г/(А∙ч)':
            q = (q/3600*1000)/1000000
    return q

def converter_t(t, units_t):
    """Конвертер времени из часов и минут в секунды."""

    if t != None:
        if units_t == 'ч':
            t = t*3600
        if units_t == 'мин':
            t = t*60
    return t


class TimeViewSet(viewsets.ModelViewSet):
    """Вьюсет для расчета времени."""

    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            m = converter_m(request.data['m'], request.data['units_m'])
            I = converter_I(request.data['I'], request.data['units_I'])
            S = converter_S(request.data['S'], request.data['units_S'])
            j = converter_j(request.data['j'], request.data['units_j'])
            p = converter_p(request.data['p'], request.data['units_p'])
            h = converter_h(request.data['h'], request.data['units_h'])
            q = converter_q(request.data['q'], request.data['units_q'])
            wt = request.data['wt']
            if m is None and I is None:
                t = (h*p)/(j*q*wt)
            if m is None and I is not None:
                t = (h*p*S)/(I*q*wt)
            if m is not None and I is None:
                t = m/(j*S*q*wt)
            if m is not None and I is not None:
                t = m/(I*q*wt)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(t=t)
            #headers = self.get_success_headers(serializer.data)
            minutes = t/60
            hours = minutes/60
            return Response(f"Время в секундах - {t}, в минутах - {minutes}, в часах - {hours}", status=status.HTTP_201_CREATED)
        except:
            return Response(Exception, status=status.HTTP_200_OK)


class ElectrochemicalEquivalentsViewSet(viewsets.ModelViewSet):
    """Вьюсет для списка материалов покрытия."""

    queryset = ElectrochemicalEquivalents.objects.all()
    serializer_class = ElectrochemicalEquivalentsSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    ordering_fields = ('name',)
    search_fields = ('name',)
    filterset_class = ElectrochemicalEquivalentsFilter
    http_method_names = ['get']


class HeightViewSet(viewsets.ModelViewSet):
    """Вьюсет для расчета толщины покрытия."""

    queryset = Height.objects.all()
    serializer_class = HeightSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            m = converter_m(request.data['m'], request.data['units_m'])
            I = converter_I(request.data['I'], request.data['units_I'])
            S = converter_S(request.data['S'], request.data['units_S'])
            j = converter_j(request.data['j'], request.data['units_j'])
            p = converter_p(request.data['p'], request.data['units_p'])
            q = converter_q(request.data['q'], request.data['units_q'])
            t = converter_t(request.data['t'], request.data['units_t'])
            wt = request.data['wt']
            if m != None:
                h = m/p*S
            else:
                if j != None:
                    h = (t*j*q*wt)/p
                else:
                    h = (t*I*q*wt)/p*S
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(h=h)
            headers = self.get_success_headers(serializer.data)
            return Response(f'{h}', status=status.HTTP_201_CREATED, headers=headers)
        except:
            return Response(Exception, status=status.HTTP_200_OK)
