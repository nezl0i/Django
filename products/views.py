from django.shortcuts import render
from datetime import datetime
# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'date': datetime.now()
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'image': 'vendor/img/products/Adidas-hoodie.png',
             'price': 6090,
             'text': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face',
             'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
             'price': 23725,
             'text': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
             'price': 3390,
             'text': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage',
             'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
             'price': 2340,
             'text': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
             'price': 13590,
             'text': 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
             'price': 2890,
             'text': 'Легкая эластичная ткань сирсакер Фактурная ткань.'},
        ]
    }
    return render(request, 'products/products.html', context)
