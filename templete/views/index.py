from django.shortcuts import render

def index(request):
    context = {}
    context['hello'] = 'hello django'
    return render(request,"index.html",context)

def head(request):
    return render(request,"head.html")