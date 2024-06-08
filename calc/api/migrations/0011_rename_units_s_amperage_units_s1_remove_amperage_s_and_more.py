# Generated by Django 4.2.10 on 2024-06-08 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_units_s_currentdensity_units_s1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amperage',
            old_name='units_S',
            new_name='units_S1',
        ),
        migrations.RemoveField(
            model_name='amperage',
            name='S',
        ),
        migrations.RemoveField(
            model_name='amperage',
            name='units_I',
        ),
        migrations.AddField(
            model_name='amperage',
            name='S1',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S10',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S11',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S12',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S13',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S14',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S15',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S16',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S17',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S18',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S19',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S2',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S20',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S4',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S5',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S6',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S7',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S8',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='S9',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Площадь покрытия'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S10',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S11',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S12',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S13',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S14',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S15',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S16',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S17',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S18',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S19',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S20',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S6',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S7',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S8',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AddField(
            model_name='amperage',
            name='units_S9',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Единицы площади'),
        ),
        migrations.AlterField(
            model_name='amperage',
            name='I',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Сила тока'),
        ),
        migrations.AlterField(
            model_name='amperage',
            name='j',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Плотность тока'),
        ),
    ]
