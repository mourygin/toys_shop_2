from django.shortcuts import render
import sqlite3

# Create your views here.
def main_page(request):
    pn = 'Добро пожаловать в наш игрушечный магазин игрушек!'
    context = {'pn': pn}
    return render(request, 'main_page.html', context)
def shop_page(request):
    pn = 'Выбери игрушку по своему вкусу!'
    context = {'pn': pn}
    return render(request, 'toy_selection.html', context)

def basket_page(request):
    pn = 'BASKET'
    context = {'pn':pn}
    return render(request,'basket.html', context)

def purchases_page(request):
    pn ='К сожалению Ваша корзина пуста...'
    contest = {'pn': pn}
    return render(request,'purchases.html',contest)

def show_ignatiy(request):
    return render(request, 'show_ignatiy.html')
def show_teddy_bear(request):
    return render(request, 'show_teddy_bear.html')
def show_cat(request):
    return render(request, 'show_cat.html')
def show_pafnutiy(request):
    return render(request, 'show_pafnutiy.html')
def basket_page(request):
    return render(request, 'basket.html')
