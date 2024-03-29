# Generated by Django 4.2.10 on 2024-02-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectrochemicalEquivalents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('q', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Электрохимический эквивалент')),
                ('p', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Плотность покрытия')),
            ],
            options={
                'verbose_name': 'Электрохимический эквивалент',
                'verbose_name_plural': 'Электрохимические эквиваленты',
                'ordering': ('name', 'q'),
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Масса покрытия')),
                ('units_m', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы массы покрытия')),
                ('I', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Сила тока')),
                ('units_I', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы силы тока')),
                ('S', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Площадь покрытия')),
                ('units_S', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади')),
                ('j', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Плотность тока')),
                ('units_j', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы плотности тока')),
                ('p', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Плотность покрытия')),
                ('units_p', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы плотности покрытия')),
                ('h', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Толщина покрытия')),
                ('units_h', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы толщины покрытия')),
                ('q', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Электрохимический эквивалент')),
                ('units_q', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы электрохимического эквивалента')),
                ('wt', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Выход по току')),
                ('t', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Расчет времени',
                'verbose_name_plural': 'Расчеты времени',
                'ordering': ('t',),
            },
        ),
    ]
