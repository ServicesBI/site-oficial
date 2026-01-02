from .models import Page


def page_context(request):
    """
    Disponibiliza a página atual para os templates,
    baseada na URL.
    """

    path = request.path.strip("/")

    # Home
    if path == "":
        slug = "home"
    else:
        slug = path.split("/")[0]

    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        page = None

    return {
        "page": page,
    }
