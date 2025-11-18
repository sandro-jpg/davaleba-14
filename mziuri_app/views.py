from django.shortcuts import render
from .models import Item

def items_list(request):
    items = Item.objects.all()    
    return render(request, 'items.html', {'items': items})



