# Generated by Django 5.0.2 on 2024-02-14 17:57

import django.db.models.deletion
import django_admin_geomap
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('theatres', 'театры'), ('cinema', 'кино'), ('museums', 'музеи')], max_length=50, verbose_name='Катeгории')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.URLField(verbose_name='Фотография')),
                ('mon_start', models.TimeField(verbose_name='Понедельник, время открытия')),
                ('mon_end', models.TimeField(verbose_name='Понедельник, время закрытия')),
                ('tue_start', models.TimeField(verbose_name='Вторник, время открытия')),
                ('tue_end', models.TimeField(verbose_name='Вторник, время закрытия')),
                ('wed_start', models.TimeField(verbose_name='Среда, время открытия')),
                ('wed_end', models.TimeField(verbose_name='Среда, время закрытия')),
                ('thu_start', models.TimeField(verbose_name='Четверг, время открытия')),
                ('thu_end', models.TimeField(verbose_name='Четверг, время закрытия')),
                ('fri_start', models.TimeField(verbose_name='Пятница, время открытия')),
                ('fri_end', models.TimeField(verbose_name='Пятница, время закрытия')),
                ('sat_start', models.TimeField(verbose_name='Суббота, время открытия')),
                ('sat_end', models.TimeField(verbose_name='Суббота, время закрытия')),
                ('sun_start', models.TimeField(blank=True, verbose_name='Воскресенье, время открытия')),
                ('sun_end', models.TimeField(blank=True, verbose_name='Воскресенье, время закрытия')),
                ('adr', models.CharField(max_length=400, verbose_name='Адрес')),
                ('desc', models.TextField(max_length=1500, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            bases=(models.Model, django_admin_geomap.GeoItem),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.URLField(verbose_name='Фотография')),
                ('datetime_start', models.DateTimeField(verbose_name='Дата начала мероприятия')),
                ('datetime_end', models.DateTimeField(verbose_name='Дата завершения мероприятия')),
                ('desc', models.TextField(max_length=1500, verbose_name='Описание')),
                ('company', models.ManyToManyField(to='KudaGo.company', verbose_name='Где проходит')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KudaGo.location'),
        ),
    ]
