from django.db import models
from ckeditor.fields import RichTextField


# ======================================================
# PÁGINAS (BASE DE TUDO)
# ======================================================
class Page(models.Model):
    PAGE_CHOICES = [
        ("home", "Home"),
        ("python", "Python"),
        ("powerbi", "Power BI"),
        ("automacoes", "Automações"),
        ("excel", "Excel"),
        ("curriculo", "Currículo"),
        ("contato", "Contato"),
    ]

    slug = models.CharField(
        max_length=30,
        choices=PAGE_CHOICES,
        unique=True,
        editable=False,          # 🔥 NÃO EDITÁVEL
        verbose_name="Página"
    )

    # ================= HERO =================
    titulo = RichTextField(verbose_name="Hero – Título")
    titulo_color = models.CharField(max_length=7, default="#ffffff")

    subtitulo = RichTextField(blank=True)
    subtitulo_color = models.CharField(max_length=7, default="#cbd5e1")

    texto = RichTextField(blank=True)
    texto_color = models.CharField(max_length=7, default="#e5e7eb")

    banner_image = models.ImageField(
        upload_to="pages/banners/",
        blank=True,
        null=True
    )

    # ================= MENU =================
    menu_conteudo = RichTextField(blank=True, null=True)
    menu_bg_color = models.CharField(max_length=7, default="#0f172a")
    menu_text_color = models.CharField(max_length=7, default="#ffffff")

    # ================= SERVIÇOS =================
    services_title_color = models.CharField(max_length=7, default="#fde047")
    services_text_color = models.CharField(max_length=7, default="#334155")
    services_border_color = models.CharField(max_length=7, default="#fde047")
    services_button_color = models.CharField(max_length=7, default="#fde047")

    # ================= PROJETOS =================
    projects_title_color = models.CharField(max_length=7, default="#fde047")
    projects_text_color = models.CharField(max_length=7, default="#334155")
    projects_border_color = models.CharField(max_length=7, default="#fde047")
    projects_button_color = models.CharField(max_length=7, default="#fde047")

    # ================= FOOTER =================
    footer_conteudo = RichTextField(blank=True, null=True)
    footer_bg_color = models.CharField(max_length=7, default="#020617")
    footer_text_color = models.CharField(max_length=7, default="#cbd5e1")

    # ================= CURRÍCULO =================
    curriculo_folha_1 = RichTextField(blank=True)
    curriculo_folha_2 = RichTextField(blank=True)
    curriculo_pdf = models.FileField(
        upload_to="curriculo/pdf/",
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return dict(self.PAGE_CHOICES).get(self.slug, self.slug)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
