from django.shortcuts import render

# Create your views here.

def index(request):
    main_p = 'Главная'
    shop_p = 'Автомобильные запчасти'
    basket_p = 'Корзина'
    context = {
        'main_p': main_p,
        'shop_p': shop_p,
        'basket_p': basket_p,
    }
    return render(request, 'index.html', context)

def main_page(request):
    return render(request, 'main_page.html')

def shop_page(request):
    return render(request, 'shop_page.html')

def basket_page(request):
    return render(request, 'basket_page.html')