from django.shortcuts import render
from datetime import datetime
import json
# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'date': datetime.now()
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open('products/fixtures/products.json') as file:
        context = json.load(file)
    return render(request, 'products/products.html', context)
