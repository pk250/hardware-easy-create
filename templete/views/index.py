from django.shortcuts import render

def index(request):
    context = {}
    context['hello'] = 'hello django'
    return render(request,"index.html",context)