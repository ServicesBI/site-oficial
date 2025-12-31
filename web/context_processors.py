from .models import SiteTheme

def site_theme(request):
    """
    Injeta o tema do site em todos os templates.
    Usa sempre o primeiro tema cadastrado.
    """
    theme = SiteTheme.objects.first()

    return {
        "site_theme": theme
    }
