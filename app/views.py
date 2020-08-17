from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse(bus_stations))


with open('data-398-2018-08-30.csv', encoding='cp1251') as data:
    reader = csv.DictReader(data)
    bus_list = []
    for row in reader:
        bus_list.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))
    paginator = Paginator(bus_list, 10)
    stations = paginator.get_page(current_page)
    prev_page, next_page = None, None
    if stations.has_previous():
        prev_page = f'bus_stations?page={stations.previous_page_number()}'
    if stations.has_next():
        next_page = f'bus_stations?page={stations.next_page_number()}'
    context = {
        'bus_stations': stations,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
        'current_page': current_page
    }
    return render(request, 'index.html', context=context)

