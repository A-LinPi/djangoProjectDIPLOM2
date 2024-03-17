from django.db import models
from django_admin_geomap import GeoItem


# Create your models here.

class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100)
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lat is None else str(self.lat)

    def __str__(self):
        return self.name


class Company(models.Model):
    CATEGORIES_CHOICES = (('theatres', 'театры'), ('cinema', 'кино'), ('museums', 'музеи'))
    category = models.CharField(verbose_name='Катeгории', choices=CATEGORIES_CHOICES, max_length=50)
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.URLField(verbose_name='Фотография')
    mon_start = models.TimeField(verbose_name='Понедельник, время открытия', null=True, blank=True)
    mon_end = models.TimeField(verbose_name='Понедельник, время закрытия', null=True, blank=True)
    tue_start = models.TimeField(verbose_name='Вторник, время открытия', null=True, blank=True)
    tue_end = models.TimeField(verbose_name='Вторник, время закрытия', null=True, blank=True)
    wed_start = models.TimeField(verbose_name='Среда, время открытия', null=True, blank=True)
    wed_end = models.TimeField(verbose_name='Среда, время закрытия', null=True)
    thu_start = models.TimeField(verbose_name='Четверг, время открытия', null=True, blank=True)
    thu_end = models.TimeField(verbose_name='Четверг, время закрытия', null=True, blank=True)
    fri_start = models.TimeField(verbose_name='Пятница, время открытия', null=True, blank=True)
    fri_end = models.TimeField(verbose_name='Пятница, время закрытия', null=True, blank=True)
    sat_start = models.TimeField(verbose_name='Суббота, время открытия', null=True, blank=True)
    sat_end = models.TimeField(verbose_name='Суббота, время закрытия', null=True, blank=True)
    sun_start = models.TimeField(blank=True, verbose_name='Воскресенье, время открытия', null=True,)
    sun_end = models.TimeField(blank=True, verbose_name='Воскресенье, время закрытия', null=True, )
    adr = models.CharField(max_length=400, verbose_name='Адрес')
    desc = models.TextField(max_length=1500, verbose_name='Описание')
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    company = models.ManyToManyField(Company, verbose_name='Где проходит')
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.URLField(verbose_name='Фотография')
    datetime_start = models.DateTimeField(verbose_name='Дата начала мероприятия')
    datetime_end = models.DateTimeField(verbose_name='Дата завершения мероприятия')
    duration_hrs = models.IntegerField(verbose_name='Продолжительность (часы)', null=True, blank=True)
    duration_min = models.IntegerField(verbose_name='Продолжительность (минуты)', null=True, blank=True)
    desc = models.TextField(max_length=1500, verbose_name='Описание')

    def __str__(self):
        return self.title

