from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
import requests

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorter = request.GET.get('sort', None)
    if not sorter or sorter == 'name':
        phones_objects = sorted(Phone.objects.all(), key=lambda Phone: Phone.name)
    elif sorter == 'min_price':
        phones_objects = sorted(Phone.objects.all(), key=lambda Phone: Phone.price)
    elif sorter == 'max_price':
        phones_objects = sorted(Phone.objects.all(), key=lambda Phone: Phone.price, reverse=True)
    template = 'catalog.html'
    context = {
        "phones": phones_objects,
    }
    return render(request, template, context=context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context=context)
