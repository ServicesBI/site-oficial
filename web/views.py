from django.shortcuts import render, get_object_or_404
from .models import Page, ServiceCard, ProjectCard, ContactContent


# ======================================================
# FUNÇÃO AUXILIAR
# ======================================================
def get_page(slug):
    return get_object_or_404(Page, slug=slug)


# ======================================================
# HOME
# ======================================================
def home(request):
    page = get_page("home")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(page=page, ativo=True).order_by("ordem")

    return render(request, "web/home.html", {
        "page": page,
        "services": services,
        "projects": projects,
    })


# ======================================================
# PYTHON
# ======================================================
def python(request):
    page = get_page("python")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(page=page, ativo=True).order_by("ordem")

    return render(request, "web/python.html", {
        "page": page,
        "services": services,
        "projects": projects,
    })


# ======================================================
# POWER BI
# ======================================================
def powerbi(request):
    page = get_page("powerbi")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(page=page, ativo=True).order_by("ordem")

    return render(request, "web/powerbi.html", {
        "page": page,
        "services": services,
        "projects": projects,
    })


# ======================================================
# AUTOMAÇÕES
# ======================================================
def automacoes(request):
    page = get_page("automacoes")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(page=page, ativo=True).order_by("ordem")

    return render(request, "web/automacoes.html", {
        "page": page,
        "services": services,
        "projects": projects,
    })


# ======================================================
# EXCEL
# ======================================================
def excel(request):
    page = get_page("excel")

    services = ServiceCard.objects.filter(page=page).order_by("ordem")
    projects = ProjectCard.objects.filter(page=page, ativo=True).order_by("ordem")

    return render(request, "web/excel.html", {
        "page": page,
        "services": services,
        "projects": projects,
    })


# ======================================================
# CURRÍCULO (SEM SERVICES / PROJECTS)
# ======================================================
def curriculo(request):
    page = get_page("curriculo")

    return render(request, "web/curriculo.html", {
        "page": page,
    })


# ======================================================
# CONTATO
# ======================================================
def contato(request):
    page = get_page("contato")
    contact = get_object_or_404(ContactContent, page=page)

    return render(request, "web/contato.html", {
        "page": page,
        "contact": contact,
    })
