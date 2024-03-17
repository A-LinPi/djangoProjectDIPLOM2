from django.shortcuts import render
from django_admin_geomap import geomap_context
# Create your views here.

from .models import Location, Event, Company


def home(request):
    return render(request, 'index.html', geomap_context(Location.objects.all(), auto_zoom=25))


def cinema_list(request):
    company_base = Company.objects.all()
    cinema_base = company_base.filter(category='cinema')
    data = {'cinema_base': cinema_base}
    return render(request, 'cinema.html', data)


def theatres_list(request):
    company_base = Company.objects.all()
    theatres_base = company_base.filter(category='theatres')
    data = {'theatres_base': theatres_base}
    return render(request, 'theatres.html', data)


def museums_list(request):
    company_base = Company.objects.all()
    museums_base = company_base.filter(category='museums')
    data = {'museums_base': museums_base}
    return render(request, 'museums.html', data)


def events_list(request):
    events_base = Event.objects.all()
    title = 'Все события'
    data = {'events_base': events_base, 'title': title}
    return render(request, 'events.html', data)


def cinema_events(request):
    events_base_cinema = Event.objects.filter(company__category='cinema').distinct()
    title = 'Только фильмы'
    data = {'events_base': events_base_cinema, 'title': title}
    return render(request, 'events.html', data)


def theatres_events(request):
    events_base_theatres = Event.objects.filter(company__category='theatres').distinct()
    title = 'Только спектакли'
    data = {'events_base': events_base_theatres, 'title': title}
    return render(request, 'events.html', data)


def contacts(request):
    return render(request, 'contacts.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
