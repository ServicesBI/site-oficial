from django.shortcuts import render

def home(request):
    return render(request, "web/home.html")

def python(request):
    return render(request, "web/python.html")

def powerbi(request):
    return render(request, "web/powerbi.html")

def automacoes(request):
    return render(request, "web/automacoes.html")

def excel(request):
    return render(request, "web/excel.html")

def curriculo(request):
    return render(request, "web/curriculo.html")

def contato(request):
    return render(request, "web/contato.html")
