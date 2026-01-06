# servicesbi/views.py

from django.shortcuts import render, get_object_or_404
from .models import Page


# =========================
# HOME
# =========================
def home(request):
    page = get_object_or_404(Page, slug="home")
    return render(request, "servicesbi/home.html", {"page": page})


# =========================
# PYTHON
# =========================
def python(request):
    page = get_object_or_404(Page, slug="python")
    return render(request, "servicesbi/python.html", {"page": page})


# =========================
# POWER BI
# =========================
def powerbi(request):
    page = get_object_or_404(Page, slug="powerbi")
    return render(request, "servicesbi/powerbi.html", {"page": page})


# =========================
# AUTOMAÇÕES
# =========================
def automacoes(request):
    page = get_object_or_404(Page, slug="automacoes")
    return render(request, "servicesbi/automacoes.html", {"page": page})


# =========================
# EXCEL
# =========================
def excel(request):
    page = get_object_or_404(Page, slug="excel")
    return render(request, "servicesbi/excel.html", {"page": page})


# =========================
# CURRÍCULO
# =========================
def curriculo(request):
    page = get_object_or_404(Page, slug="curriculo")
    return render(request, "servicesbi/curriculo.html", {"page": page})


# =========================
# CONTATO
# =========================
def contato(request):
    page = get_object_or_404(Page, slug="contato")
    return render(request, "servicesbi/contato.html", {"page": page})
