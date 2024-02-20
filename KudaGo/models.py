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
    #
    # @property
    # def geomap_popup_view(self):
    #     return "<strong>{}</strong>".format(str(self))
    #
    # @property
    # def geomap_popup_edit(self):
    #     return self.geomap_popup_view
    #
    # @property
    # def geomap_popup_common(self):
    #     return self.geomap_popup_view

    def __str__(self):
        return self.name


class Company(models.Model):
    CATEGORIES_CHOICES = (('theatres', 'театры'), ('cinema', 'кино'), ('museums', 'музеи'))
    category = models.CharField(verbose_name='Катeгории', choices=CATEGORIES_CHOICES, max_length=50)
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.URLField(verbose_name='Фотография')
    mon_start = models.TimeField(verbose_name='Понедельник, время открытия')
    mon_end = models.TimeField(verbose_name='Понедельник, время закрытия')
    tue_start = models.TimeField(verbose_name='Вторник, время открытия')
    tue_end = models.TimeField(verbose_name='Вторник, время закрытия')
    wed_start = models.TimeField(verbose_name='Среда, время открытия')
    wed_end = models.TimeField(verbose_name='Среда, время закрытия')
    thu_start = models.TimeField(verbose_name='Четверг, время открытия')
    thu_end = models.TimeField(verbose_name='Четверг, время закрытия')
    fri_start = models.TimeField(verbose_name='Пятница, время открытия')
    fri_end = models.TimeField(verbose_name='Пятница, время закрытия')
    sat_start = models.TimeField(verbose_name='Суббота, время открытия')
    sat_end = models.TimeField(verbose_name='Суббота, время закрытия')
    sun_start = models.TimeField(blank=True, verbose_name='Воскресенье, время открытия')
    sun_end = models.TimeField(blank=True, verbose_name='Воскресенье, время закрытия')
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
    desc = models.TextField(max_length=1500, verbose_name='Описание')

    def __str__(self):
        return self.title

