from .models import Page


def page_context(request):
    """
    Disponibiliza a página atual e o theme (cores)
    para todos os templates, baseado na URL.
    """

    path = request.path.strip("/")

    # =============================
    # DEFINIÇÃO DO SLUG DA PÁGINA
    # =============================
    if path == "":
        slug = "home"
    else:
        slug = path.split("/")[0]

    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        page = None

    # =============================
    # THEME (CORES DINÂMICAS)
    # =============================
    if page:
        theme = {
            # MENU
            "menu_bg_color": page.menu_bg_color,
            "menu_text_color": page.menu_text_color,

            # HERO
            "title_color": page.titulo_color,
            "subtitle_color": page.subtitulo_color,
            "text_color": page.texto_color,

            # SERVIÇOS
            "services_title_color": page.services_title_color,
            "services_text_color": page.services_text_color,
            "services_border_color": page.services_border_color,
            "services_button_color": page.services_button_color,

            # PROJETOS
            "projects_title_color": page.projects_title_color,
            "projects_text_color": page.projects_text_color,
            "projects_border_color": page.projects_border_color,
            "projects_button_color": page.projects_button_color,

            # FOOTER  ← ALTERAÇÃO
            "footer_bg_color": page.footer_bg_color,
            "footer_text_color": page.footer_text_color,
        }
    else:
        theme = {}

    return {
        "page": page,
        "theme": theme,
    }
