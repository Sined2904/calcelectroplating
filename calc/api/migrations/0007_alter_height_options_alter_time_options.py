# Generated by Django 4.2.10 on 2024-03-31 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_height_options_alter_time_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='height',
            options={'ordering': ('id',), 'verbose_name': 'Расчет толщины покрытия', 'verbose_name_plural': 'Расчеты толщин покрытия'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'ordering': ('id',), 'verbose_name': 'Расчет времени', 'verbose_name_plural': 'Расчеты времени'},
        ),
    ]
