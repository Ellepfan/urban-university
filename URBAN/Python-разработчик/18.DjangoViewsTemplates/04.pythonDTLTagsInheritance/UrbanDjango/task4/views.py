from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def menu(request):
    main = 'Главная'
    shop = 'Автомобильные запчасти'
    basket = 'Корзина'
    context = {
        'main': main,
        'shop': shop,
        'basket': basket,
    }
    return render(request, 'menu.html', context)


def main_page(request):
    # main = 'Главная'
    # shop = 'Автомобильные запчасти'
    # basket = 'Корзина'
    # context = {
    #     'main': main,
    #     'shop': shop,
    #     'basket': basket,
    # }
    return render(request, 'fourth_task/main_page.html')

def shop_page(request):
    parts = ["Двигатель", "Кузов","Ходовая часть"]
    context = {
        'parts': parts,
    }
    return render(request, 'fourth_task/shop_page.html', context)

def basket_page(request):
    return render(request, 'fourth_task/basket_page.html')