from django.shortcuts import render, get_object_or_404

from .models import (
    Page,
    PageTheme,
    ServiceCard,
    ProjectCard,
    ContactContent,
)


# ======================================================
# FUNÇÃO AUXILIAR
# ======================================================
def get_page(slug):
    page = get_object_or_404(Page, slug=slug)
    theme = getattr(page, "theme", None)
    return page, theme


# ======================================================
# HOME
# ======================================================
def home(request):
    page, theme = get_page("home")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(
        page=page,
        ativo=True
    ).order_by("ordem")

    return render(request, "web/home.html", {
        "page": page,
        "theme": theme,
        "services": services,
        "projects": projects,
    })


# ======================================================
# PÁGINAS DE SERVIÇOS
# ======================================================
def python(request):
    page, theme = get_page("python")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(
        page=page,
        ativo=True
    ).order_by("ordem")

    return render(request, "web/python.html", {
        "page": page,
        "theme": theme,
        "services": services,
        "projects": projects,
    })


def powerbi(request):
    page, theme = get_page("powerbi")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(
        page=page,
        ativo=True
    ).order_by("ordem")

    return render(request, "web/powerbi.html", {
        "page": page,
        "theme": theme,
        "services": services,
        "projects": projects,
    })


def automacoes(request):
    page, theme = get_page("automacoes")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(
        page=page,
        ativo=True
    ).order_by("ordem")

    return render(request, "web/automacoes.html", {
        "page": page,
        "theme": theme,
        "services": services,
        "projects": projects,
    })


def excel(request):
    page, theme = get_page("excel")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(
        page=page,
        ativo=True
    ).order_by("ordem")

    return render(request, "web/excel.html", {
        "page": page,
        "theme": theme,
        "services": services,
        "projects": projects,
    })


# ======================================================
# CURRÍCULO (AGORA É PAGE NORMAL)
# ======================================================
def curriculo(request):
    page, theme = get_page("curriculo")

    return render(request, "web/curriculo.html", {
        "page": page,
        "theme": theme,
    })


# ======================================================
# CONTATO
# ======================================================
def contato(request):
    page, theme = get_page("contato")
    contact = get_object_or_404(ContactContent, page=page)

    return render(request, "web/contato.html", {
        "page": page,
        "theme": theme,
        "contact": contact,
    })
