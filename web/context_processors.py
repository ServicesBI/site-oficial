from .models import Page, PageTheme


def site_theme(request):
    """
    Retorna o tema do site baseado na página atual.
    Prioridade:
    1) Tema específico da página
    2) Tema global
    """

    # Tema global (fallback)
    theme = PageTheme.objects.filter(page__slug="home").first()

    path = request.path.strip("/").lower()

    # HOME (caso especial)
    if path == "":
        page = Page.objects.filter(slug="home").first()
        if page and hasattr(page, "theme"):
            theme = page.theme

        return {
            "theme": theme,
            "page": page,
        }

    # Outras páginas
    page = Page.objects.filter(slug=path).first()

    if page and hasattr(page, "theme"):
        theme = page.theme

    return {
        "theme": theme,
        "page": page,
    }
