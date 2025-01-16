from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def main_page(request):
    main = 'Главная'
    shop = 'Автомобильные запчасти'
    basket = 'Корзина'
    context = {
        'main': main,
        'shop': shop,
        'basket': basket,
    }
    return render(request, 'main_page.html', context)

def shop_page(request):
    return render(request, 'shop_page.html')

def basket_page(request):
    return render(request, 'basket_page.html')