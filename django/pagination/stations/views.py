import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    objects = []
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            objects.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    paginator = Paginator(objects, 25)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'page': page,
        'bus_stations': page.object_list
    }

    return render(request, 'stations/index.html', context)
