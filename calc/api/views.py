from django.shortcuts import render
from .models import Time, ElectrochemicalEquivalents, Height, Weight, CurrentDensity, Amperage
from rest_framework.response import Response
from .serializers import TimeSerializer, ElectrochemicalEquivalentsSerializer, HeightSerializer, TimeSerializerOutput, HeigthSerializerOutput, WeightSerializer, WeigthSerializerOutput, CurrentDensitySerializer, CurrentDensitySerializerOutput, AmperageSerializer, AmperageSerializerOutput
from .filters import ElectrochemicalEquivalentsFilter
from rest_framework import viewsets, filters, status
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.exceptions import APIException


class AnswerLessOne(APIException):
    status_code = 400
    default_detail = 'Ответ меньше одной секунды'
    default_code = 'answer_less_one'


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

    if S == None:
        S = 0
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
        if units_p == 'г/см3':
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
            print(t)
            if t<1:
                raise AnswerLessOne()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(t=t)
            return Response(TimeSerializerOutput(Time.objects.last()).data, status=status.HTTP_201_CREATED)
        except AnswerLessOne:
            raise AnswerLessOne('Ответ меньше секунды!')
        except Exception as err:
            return HttpResponse(f'При обработке возникла ошибка: {err}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
                h = m/(p*S)
            else:
                if j != None:
                    h = (t*j*q*wt)/p
                else:
                    h = (t*I*q*wt)/(p*S)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(h=h*1000000) #Перевод в микрометры
            headers = self.get_success_headers(serializer.data)
            return Response(HeigthSerializerOutput(Height.objects.last()).data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return HttpResponse(f'При обработке возникла ошибка: {err}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class WeightViewSet(viewsets.ModelViewSet):
    """Вьюсет для расчета массы."""

    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            I = converter_I(request.data['I'], request.data['units_I'])
            S = converter_S(request.data['S'], request.data['units_S'])
            t = converter_t(request.data['t'], request.data['units_t'])
            j = converter_j(request.data['j'], request.data['units_j'])
            p = converter_p(request.data['p'], request.data['units_p'])
            h = converter_h(request.data['h'], request.data['units_h'])
            q = converter_q(request.data['q'], request.data['units_q'])
            wt = request.data['wt']
            if h is not None:
                m = S*p*h
            if I is not None:
                m = I*t*q*wt
            if j is not None:
                m = j*S*t*q*wt
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(m=m*1000000) #Перевод в мг
            return Response(WeigthSerializerOutput(Weight.objects.last()).data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return HttpResponse(f'При обработке возникла ошибка: {err}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrentDensityViewSet(viewsets.ModelViewSet):
    """Вьюсет для расчета плотности тока."""

    queryset = CurrentDensity.objects.all()
    serializer_class = CurrentDensitySerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            I = converter_I(request.data['I'], request.data['units_I'])
            S1 = converter_S(request.data['S1'], request.data['units_S1'])
            S2 = converter_S(request.data['S2'], request.data['units_S2'])
            S3 = converter_S(request.data['S3'], request.data['units_S3'])
            S4 = converter_S(request.data['S4'], request.data['units_S4'])
            S5 = converter_S(request.data['S5'], request.data['units_S5'])
            S6 = converter_S(request.data['S6'], request.data['units_S6'])
            S7 = converter_S(request.data['S7'], request.data['units_S7'])
            S8 = converter_S(request.data['S8'], request.data['units_S8'])
            S9 = converter_S(request.data['S9'], request.data['units_S9'])
            S10 = converter_S(request.data['S10'], request.data['units_S10'])
            S11 = converter_S(request.data['S11'], request.data['units_S11'])
            S12 = converter_S(request.data['S12'], request.data['units_S12'])
            S13 = converter_S(request.data['S13'], request.data['units_S13'])
            S14 = converter_S(request.data['S14'], request.data['units_S14'])
            S15 = converter_S(request.data['S15'], request.data['units_S15'])
            S16 = converter_S(request.data['S16'], request.data['units_S16'])
            S17 = converter_S(request.data['S17'], request.data['units_S17'])
            S18 = converter_S(request.data['S18'], request.data['units_S18'])
            S19 = converter_S(request.data['S19'], request.data['units_S19'])
            S20 = converter_S(request.data['S20'], request.data['units_S20'])
            j = (I/(S1+S2+S3+S4+S5+S6+S7+S8+S9+S10+S11+S12+S13+S14+S15+S16+S17+S18+S19+S20))/100
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(j=j)
            headers = self.get_success_headers(serializer.data)
            return Response(CurrentDensitySerializerOutput(CurrentDensity.objects.last()).data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return HttpResponse(f'При обработке возникла ошибка: {err}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AmperageViewSet(viewsets.ModelViewSet):
    """Вьюсет для расчета силы тока."""

    queryset = Amperage.objects.all()
    serializer_class = AmperageSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        try:
            j = converter_I(request.data['j'], request.data['units_j'])
            S1 = converter_S(request.data['S1'], request.data['units_S1'])
            S2 = converter_S(request.data['S2'], request.data['units_S2'])
            S3 = converter_S(request.data['S3'], request.data['units_S3'])
            S4 = converter_S(request.data['S4'], request.data['units_S4'])
            S5 = converter_S(request.data['S5'], request.data['units_S5'])
            S6 = converter_S(request.data['S6'], request.data['units_S6'])
            S7 = converter_S(request.data['S7'], request.data['units_S7'])
            S8 = converter_S(request.data['S8'], request.data['units_S8'])
            S9 = converter_S(request.data['S9'], request.data['units_S9'])
            S10 = converter_S(request.data['S10'], request.data['units_S10'])
            S11 = converter_S(request.data['S11'], request.data['units_S11'])
            S12 = converter_S(request.data['S12'], request.data['units_S12'])
            S13 = converter_S(request.data['S13'], request.data['units_S13'])
            S14 = converter_S(request.data['S14'], request.data['units_S14'])
            S15 = converter_S(request.data['S15'], request.data['units_S15'])
            S16 = converter_S(request.data['S16'], request.data['units_S16'])
            S17 = converter_S(request.data['S17'], request.data['units_S17'])
            S18 = converter_S(request.data['S18'], request.data['units_S18'])
            S19 = converter_S(request.data['S19'], request.data['units_S19'])
            S20 = converter_S(request.data['S20'], request.data['units_S20'])
            I = j*(S1+S2+S3+S4+S5+S6+S7+S8+S9+S10+S11+S12+S13+S14+S15+S16+S17+S18+S19+S20)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(I=I)
            headers = self.get_success_headers(serializer.data)
            return Response(AmperageSerializerOutput(Amperage.objects.last()).data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return HttpResponse(f'При обработке возникла ошибка: {err}', status=status.HTTP_500_INTERNAL_SERVER_ERROR)