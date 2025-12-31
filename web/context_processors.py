from .models import SiteTheme

def site_theme(request):
    """
    Retorna o tema do site baseado na página atual.
    Prioridade:
    1) Tema específico da página
    2) Tema global
    """

    # Tema global (fallback)
    theme = SiteTheme.objects.filter(pagina="global").first()

    path = request.path.lower()

    # ✅ HOME (caso especial)
    if path == "/":
        home_theme = SiteTheme.objects.filter(pagina="home").first()
        if home_theme:
            theme = home_theme

        return {
            "site_theme": theme
        }

    # Mapeamento por URL
    page_map = {
        "curriculo": "curriculo",
        "contato": "contato",
        "python": "python",
        "powerbi": "powerbi",
        "automacoes": "automacoes",
        "excel": "excel",
    }

    for key, page in page_map.items():
        if key in path:
            page_theme = SiteTheme.objects.filter(pagina=page).first()
            if page_theme:
                theme = page_theme
            break

    return {
        "site_theme": theme
    }
