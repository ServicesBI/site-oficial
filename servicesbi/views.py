from django.shortcuts import render

def home(request):
    return render(request, "servicesbi/index.html")

def python(request):
    return render(request, "servicesbi/python.html")

def powerbi(request):
    return render(request, "servicesbi/powerbi.html")

def automacoes(request):
    return render(request, "servicesbi/automacoes.html")

def excel(request):
    return render(request, "servicesbi/excel.html")

def curriculo(request):
    return render(request, "servicesbi/curriculo.html")

def contato(request):
    return render(request, "servicesbi/contato.html")
