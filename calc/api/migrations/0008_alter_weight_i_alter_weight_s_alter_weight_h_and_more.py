# Generated by Django 4.2.10 on 2024-05-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_height_options_alter_time_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='I',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Сила тока'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='S',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='h',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Толщина покрытия'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='j',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Плотность тока'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='m',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Масса покрытия'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='p',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Плотность покрытия'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='q',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Электрохимический эквивалент'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='t',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Время покрытия'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='wt',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Выход по току'),
        ),
    ]