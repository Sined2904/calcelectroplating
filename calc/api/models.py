from django.db import models


class Time(models.Model):
    """Модель расчета времени покрытия."""

    m = models.DecimalField('Масса покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_m = models.CharField('Единицы массы покрытия', max_length=50, blank=True, null=True)
    I = models.DecimalField('Сила тока', max_digits=15, decimal_places=4, blank=True, null=True)
    units_I = models.CharField('Единицы силы тока', max_length=50, blank=True, null=True)
    S = models.DecimalField('Площадь покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_S = models.CharField('Единицы площади', max_length=50, blank=True, null=True)
    j = models.DecimalField('Плотность тока', max_digits=15, decimal_places=4, blank=True, null=True)
    units_j = models.CharField('Единицы плотности тока', max_length=50, blank=True, null=True)
    p = models.DecimalField('Плотность покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_p = models.CharField('Единицы плотности покрытия', max_length=50, blank=True, null=True)
    h = models.DecimalField('Толщина покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_h = models.CharField('Единицы толщины покрытия', max_length=50, blank=True, null=True)
    q = models.DecimalField('Электрохимический эквивалент', max_digits=15, decimal_places=4, blank=True, null=True)
    units_q = models.CharField('Единицы электрохимического эквивалента', max_length=50, blank=True, null=True)
    wt = models.DecimalField('Выход по току', max_digits=15, decimal_places=4, blank=True, null=True)
    t = models.DecimalField('Время', max_digits=15, decimal_places=4, blank=True, null=True)

    class Meta:
        ordering = ('id', )
        verbose_name = "Расчет времени"
        verbose_name_plural = "Расчеты времени"

    def __str__(self):
        return f"Расчет времени покрытия №{self.id}"


class ElectrochemicalEquivalents(models.Model):
    """Модель электрохимических эквивалентов."""

    name = models.CharField('Название', max_length=50)
    q = models.DecimalField('Электрохимический эквивалент (мг/кулон)', max_digits=12, decimal_places=4, blank=True, null=True)
    p = models.DecimalField('Плотность покрытия (кг/м3)', max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        ordering = ('name', 'q')
        verbose_name = "Материал покрытия"
        verbose_name_plural = "Материалы покрытия"

    def __str__(self):
        return self.name


class Height(models.Model):
    """Модель расчета толщины покрытия."""

    v = models.DecimalField('Скорость осаждения', max_digits=15, decimal_places=4, blank=True, null=True)
    units_v = models.CharField('Единицы скорости осаждения', max_length=50, blank=True, null=True)
    j = models.DecimalField('Плотность тока', max_digits=15, decimal_places=4, blank=True, null=True)
    units_j = models.CharField('Единицы плотности тока', max_length=50, blank=True, null=True)
    t = models.DecimalField('Время покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_t = models.CharField('Единицы времени покрытия', max_length=50, blank=True, null=True)
    p = models.DecimalField('Плотность покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_p = models.CharField('Единицы плотности покрытия', max_length=50, blank=True, null=True)
    q = models.DecimalField('Электрохимический эквивалент', max_digits=15, decimal_places=4, blank=True, null=True)
    units_q = models.CharField('Единицы электрохимического эквивалента', max_length=50, blank=True, null=True)
    wt = models.DecimalField('Выход по току', max_digits=15, decimal_places=4, blank=True, null=True)
    I = models.DecimalField('Сила тока', max_digits=15, decimal_places=4, blank=True, null=True)
    units_I = models.CharField('Единицы силы тока', max_length=50, blank=True, null=True)
    S = models.DecimalField('Площадь покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_S = models.CharField('Единицы площади', max_length=50, blank=True, null=True)
    m = models.DecimalField('Масса покрытия', max_digits=15, decimal_places=4, blank=True, null=True)
    units_m = models.CharField('Единицы массы покрытия', max_length=50, blank=True, null=True)
    h = models.DecimalField('Толщина покрытия (в метрах)', max_digits=15, decimal_places=4, blank=True, null=True)    

    class Meta:
        ordering = ('id', )
        verbose_name = "Расчет толщины покрытия"
        verbose_name_plural = "Расчеты толщин покрытия"

    def __str__(self):
        return f"Расчет толщины покрытия №{self.id}"


class Weight(models.Model):
    """Модель расчета массы покрытия."""

    I = models.DecimalField('Сила тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_I = models.CharField('Единицы силы тока', max_length=50, blank=True, null=True)
    t = models.DecimalField('Время покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_t = models.CharField('Единицы времени покрытия', max_length=50, blank=True, null=True)
    q = models.DecimalField('Электрохимический эквивалент', max_digits=12, decimal_places=3, blank=True, null=True)
    units_q = models.CharField('Единицы электрохимического эквивалента', max_length=50, blank=True, null=True)
    wt = models.DecimalField('Выход по току', max_digits=12, decimal_places=3, blank=True, null=True)
    j = models.DecimalField('Плотность тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_j = models.CharField('Единицы плотности тока', max_length=50, blank=True, null=True)
    S = models.DecimalField('Площадь покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_S = models.CharField('Единицы площади', max_length=50, blank=True, null=True)
    p = models.DecimalField('Плотность покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_p = models.CharField('Единицы плотности покрытия', max_length=50, blank=True, null=True)
    h = models.DecimalField('Толщина покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_h = models.CharField('Единицы толщины покрытия', max_length=50, blank=True, null=True)
    m = models.DecimalField('Масса покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
 
    class Meta:
        ordering = ('id', )
        verbose_name = "Расчет массы покрытия"
        verbose_name_plural = "Расчеты масс покрытия"

    def __str__(self):
        return f"Расчет массы покрытия №{self.id}"


class CurrentDensity(models.Model):
    """Модель расчета плотности тока."""

    S = models.DecimalField('Площадь покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_S = models.CharField('Единицы площади', max_length=50, blank=True, null=True)
    j = models.DecimalField('Плотность тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_j = models.CharField('Единицы плотности тока', max_length=50, blank=True, null=True)
    I = models.DecimalField('Сила тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_I = models.CharField('Единицы силы тока', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('id', )
        verbose_name = "Расчет плотности тока"
        verbose_name_plural = "Расчеты плотностей тока"

    def __str__(self):
        return f"Расчет плотности тока №{self.id}"


class Amperage(models.Model):
    """Модель расчета силы тока."""

    S = models.DecimalField('Площадь покрытия', max_digits=12, decimal_places=3, blank=True, null=True)
    units_S = models.CharField('Единицы площади', max_length=50, blank=True, null=True)
    j = models.DecimalField('Плотность тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_j = models.CharField('Единицы плотности тока', max_length=50, blank=True, null=True)
    I = models.DecimalField('Сила тока', max_digits=12, decimal_places=3, blank=True, null=True)
    units_I = models.CharField('Единицы силы тока', max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('id', )
        verbose_name = "Расчет силы тока"
        verbose_name_plural = "Расчеты сил тока"

    def __str__(self):
        return f"Расчет силы тока №{self.id}"