from django.shortcuts import render

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categorias = Category.objects.all()
    return render(request, 'marketplace/index.html', {
        'categorias': categorias,
        'items': items,
    })

def contact(request):
    return render(request, 'marketplace/contact.html')

def signup(request):
    form = SignupForm
    return render(request, 'marketplace/signup.html', {
        'form': form
    })