"""
URL configuration for djangoProjectDIPLOM2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from KudaGo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('events/all', views.events_list, name='all_events'),
    path('cinema/all', views.cinema_list, name='all_cinema'),
    path('theatres/all', views.theatres_list, name='all_theatres'),
    path('museums/all', views.museums_list, name='all_museums'),
    path('events/all/cinema', views.cinema_events, name='only_cinema'),
]
