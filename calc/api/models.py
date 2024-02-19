from django.db import models


class Time(models.Model):
    """Модель расчета времени покрытия."""

    m = models.DecimalField('Масса покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_m = models.CharField('Единицы массы покрытия', max_length=50, blank=True, null=True)
    I = models.DecimalField('Сила тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_I = models.CharField('Единицы силы тока', max_length=50, blank=True, null=True)
    S = models.DecimalField('Площадь покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_S = models.CharField('Единицы площади', max_length=50, blank=True, null=True)
    j = models.DecimalField('Плотность тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_j = models.CharField('Единицы плотности тока', max_length=50, blank=True, null=True)
    p = models.DecimalField('Плотность покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_p = models.CharField('Единицы плотности покрытия', max_length=50, blank=True, null=True)
    h = models.DecimalField('Толщина покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_h = models.CharField('Единицы толщины покрытия', max_length=50, blank=True, null=True)
    q = models.DecimalField('Электрохимический эквивалент', max_digits=12, decimal_places=3, blank=True, null=True)
    units_q = models.CharField('Единицы электрохимического эквивалента', max_length=50, blank=True, null=True)
    wt = models.DecimalField('Выход по току', max_digits=12, decimal_places=3, blank=True, null=True)
    t = models.DecimalField('Время', max_digits=12, decimal_places=3, blank=True, null=True)


    class Meta:
        ordering = ('t', )
        verbose_name = "Расчет времени"
        verbose_name_plural = "Расчеты времени"


class ElectrochemicalEquivalents(models.Model):
    """Модель электрохимических эквивалентов."""

    name = models.CharField('Название', max_length=50)
    q = models.DecimalField('Электрохимический эквивалент (мг/кулон)', max_digits=12, decimal_places=3, blank=True, null=True)
    p = models.DecimalField('Плотность покрытия (кг/м3)', max_digits=12, decimal_places=3, blank=True, null=True)

    class Meta:
        ordering = ('name', 'q')
        verbose_name = "Материал покрытия"
        verbose_name_plural = "Материалы покрытия"
