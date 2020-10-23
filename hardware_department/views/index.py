from django.shortcuts import render
from hardware_department.models.menu import Menu

def index(request):
    menu_list = Menu.objects.all()
    context = {
        'menu_list':menu_list
    }
    
    return render(request,"index.html",context)

def head(request):
    return render(request,"head.html")