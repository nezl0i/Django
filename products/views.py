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
        json_product = json.load(file)
    context = {
        "title": "GeekShop - Каталог",
        "products": json_product
    }
    return render(request, 'products/products.html', context)
