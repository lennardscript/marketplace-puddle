from django.shortcuts import render

def index(request):
    return render(request, 'marketplace/index.html')

def contact(request):
    return render(request, 'marketplace/contact.html')