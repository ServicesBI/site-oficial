from django.shortcuts import render, get_object_or_404
from .models import Page, ServiceCard, ProjectCard, ContactContent


# ======================================================
# VIEW GENÉRICA POR SLUG (CMS CENTRAL)
# ======================================================
def page_by_slug(request, slug=None):
    """
    VIEW GENÉRICA DO CMS

    Regras:
    - '/'            → home
    - '/<slug>/'     → Page(slug=slug)
    - Algumas páginas possuem comportamento especial
    """

    # ==================================================
    # SLUG PADRÃO
    # ==================================================
    page_slug = slug if slug else "home"

    page = get_object_or_404(Page, slug=page_slug)

    # ==================================================
    # PÁGINAS ESPECIAIS (LÓGICA PRÓPRIA)
    # ==================================================

    # CONTATO
    if page_slug == "contato":
        contact = get_object_or_404(ContactContent, page=page)
        return render(request, "web/contato.html", {
            "page": page,
            "contact": contact,
        })

    # CURRÍCULO (não possui services / projects)
    if page_slug == "curriculo":
        return render(request, "web/curriculo.html", {
            "page": page,
        })

    # ==================================================
    # PÁGINAS PADRÃO (CMS)
    # ==================================================
    services = ServiceCard.objects.filter(
        page=page
    ).order_by("ordem")

    projects = ProjectCard.objects.filter(
        page=page,
        ativo=True
    ).order_by("ordem")

    return render(request, "web/page.html", {
        "page": page,
        "services": services,
        "projects": projects,
    })
