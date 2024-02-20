from django.shortcuts import render
from django_admin_geomap import geomap_context
# Create your views here.

from .models import Location, Event, Company


def home(request):
    return render(request, 'index.html', geomap_context(Location.objects.all(), auto_zoom=25))


def events_list(request):
    events_base = Event.objects.all()
    data = {'events_base': events_base}
    return render(request, 'events.html', data)


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