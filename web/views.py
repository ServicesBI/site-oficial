from django.shortcuts import render

from projects.models import Project
from .models import (
    HomeContent,
    PageContent,
    Curriculo,
    ContactContent,
    Service,
)


# ======================================================
# HOME
# ======================================================
def home(request):
    projects = Project.objects.filter(
        page='home',
        is_active=True
    ).order_by('order')

    home_content = HomeContent.objects.first()
    services = Service.objects.all().order_by('ordem')

    return render(request, "web/home.html", {
        "projects": projects,
        "home": home_content,
        "services": services,
    })


# ======================================================
# PÁGINAS DE SERVIÇOS
# ======================================================
def python(request):
    projects = Project.objects.filter(
        page='python',
        is_active=True
    ).order_by('order')

    page_content = PageContent.objects.filter(pagina='python').first()

    return render(request, "web/python.html", {
        "projects": projects,
        "page": page_content,
    })


def powerbi(request):
    projects = Project.objects.filter(
        page='powerbi',
        is_active=True
    ).order_by('order')

    page_content = PageContent.objects.filter(pagina='powerbi').first()

    return render(request, "web/powerbi.html", {
        "projects": projects,
        "page": page_content,
    })


def automacoes(request):
    projects = Project.objects.filter(
        page='automacoes',
        is_active=True
    ).order_by('order')

    page_content = PageContent.objects.filter(pagina='automacoes').first()

    return render(request, "web/automacoes.html", {
        "projects": projects,
        "page": page_content,
    })


def excel(request):
    projects = Project.objects.filter(
        page='excel',
        is_active=True
    ).order_by('order')

    page_content = PageContent.objects.filter(pagina='excel').first()

    return render(request, "web/excel.html", {
        "projects": projects,
        "page": page_content,
    })


# ======================================================
# CURRÍCULO
# ======================================================
def curriculo_view(request):
    curriculo = Curriculo.objects.first()

    return render(request, "web/curriculo.html", {
        "curriculo": curriculo
    })


# ======================================================
# CONTATO
# ======================================================
def contato(request):
    contact = ContactContent.objects.first()

    return render(request, "web/contato.html", {
        "contact": contact
    })
