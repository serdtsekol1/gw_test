from django.http import JsonResponse
from django.shortcuts import render

products_search = [
    {'id': 1, 'name': 'Product 1', 'price': 100, 'price_old': 150, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 2, 'name': 'Product 2', 'price': 200, 'price_old': 250, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 3, 'name': 'Product 3', 'price': 300, 'price_old': 350, 'image': 'https://picsum.photos/60/70', 'available': False},
    {'id': 4, 'name': 'Product 4', 'price': 400, 'price_old': 450, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 5, 'name': 'Product 5', 'price': 500, 'price_old': 550, 'image': 'https://picsum.photos/60/70', 'available': False},
    {'id': 6, 'name': 'Product 6', 'price': 600, 'price_old': 650, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 7, 'name': 'Product 7', 'price': 700, 'price_old': 750, 'image': 'https://picsum.photos/60/70', 'available': False},
    {'id': 8, 'name': 'Product 8', 'price': 800, 'price_old': 850, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 9, 'name': 'Product 9', 'price': 900, 'price_old': 950, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 10, 'name': 'Product 10', 'price': 1000, 'price_old': 1050, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 11, 'name': 'Product 11', 'price': 1100, 'price_old': 1150, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 12, 'name': 'Product 12', 'price': 1200, 'price_old': 1250, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 13, 'name': 'Product 13', 'price': 1300, 'price_old': 1350, 'image': 'https://picsum.photos/60/70', 'available': False},
    {'id': 14, 'name': 'Product 14', 'price': 1400, 'price_old': 1450, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 15, 'name': 'Product 15', 'price': 1500, 'price_old': 1550, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 16, 'name': 'Product 16', 'price': 1600, 'price_old': 1650, 'image': 'https://picsum.photos/60/70', 'available': True},
    {'id': 17, 'name': 'Product 17', 'price': 1700, 'price_old': 1750, 'image': 'https://picsum.photos/60/70', 'available': True},
]

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET.get('query', '').strip().lower()
    if not query:
        return JsonResponse([], safe=False)

    results = [
        product for product in products_search
        if query in product['name'].lower()
    ][:10]

    return JsonResponse(results, safe=False)