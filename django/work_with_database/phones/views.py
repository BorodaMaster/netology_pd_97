from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    phone_objects = Phone.objects.all()
    phones = phones_sorted = [element for element in phone_objects.values()]

    if sort == "name":
        phones_sorted = sorted(phones, key=lambda d: d['name'])
    elif sort == "min_price":
        phones_sorted = sorted(phones, key=lambda d: d['price'])
    elif sort == "max_price":
        phones_sorted = sorted(phones, key=lambda d: d['price'], reverse=True)

    context = {'phones': phones_sorted}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone_object = Phone.objects.filter(slug=slug)
    context = {'phone': element for element in phone_object.values()}

    return render(request, template, context)
