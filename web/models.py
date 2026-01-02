from django.db import models
from ckeditor.fields import RichTextField


# ======================================================
# PÁGINAS (CMS BASE)
# ======================================================
class Page(models.Model):
    """
    Page é a base de TODAS as páginas do site.
    Cada página existe UMA ÚNICA VEZ por slug.
    Ex: home, python, powerbi, etc.
    """

    slug = models.SlugField(
        max_length=30,
        unique=True,
        verbose_name="Slug da página (ex: home, python, powerbi)"
    )

    # ================= HERO =================
    titulo = RichTextField(
        verbose_name="Hero – Título"
    )
    titulo_color = models.CharField(
        max_length=7,
        default="#ffffff",
        verbose_name="Cor do título"
    )

    subtitulo = RichTextField(
        blank=True,
        verbose_name="Hero – Subtítulo"
    )
    subtitulo_color = models.CharField(
        max_length=7,
        default="#cbd5e1",
        verbose_name="Cor do subtítulo"
    )

    texto = RichTextField(
        blank=True,
        verbose_name="Texto principal"
    )
    texto_color = models.CharField(
        max_length=7,
        default="#e5e7eb",
        verbose_name="Cor do texto"
    )

    banner_image = models.ImageField(
        upload_to="pages/banners/",
        blank=True,
        null=True,
        verbose_name="Banner da página"
    )

    # ================= MENU =================
    menu_conteudo = RichTextField(
        blank=True,
        null=True,
        verbose_name="Menu – Conteúdo"
    )
    menu_bg_color = models.CharField(
        max_length=7,
        default="#0f172a",
        verbose_name="Menu – Cor de fundo"
    )
    menu_text_color = models.CharField(
        max_length=7,
        default="#ffffff",
        verbose_name="Menu – Cor do texto"
    )

    # ================= SERVIÇOS =================
    services_title_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Serviços – Título"
    )
    services_text_color = models.CharField(
        max_length=7,
        default="#334155",
        verbose_name="Serviços – Texto"
    )
    services_border_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Serviços – Borda"
    )
    services_button_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Serviços – Botão"
    )

    # ================= PROJETOS =================
    projects_title_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Projetos – Título"
    )
    projects_text_color = models.CharField(
        max_length=7,
        default="#334155",
        verbose_name="Projetos – Texto"
    )
    projects_border_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Projetos – Borda"
    )
    projects_button_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Projetos – Botão"
    )

    # ================= FOOTER =================
    footer_conteudo = RichTextField(
        blank=True,
        null=True,
        verbose_name="Footer – Conteúdo"
    )
    footer_bg_color = models.CharField(
        max_length=7,
        default="#020617",
        verbose_name="Footer – Cor de fundo"
    )
    footer_text_color = models.CharField(
        max_length=7,
        default="#cbd5e1",
        verbose_name="Footer – Cor do texto"
    )

    # ================= CURRÍCULO =================
    curriculo_folha_1 = RichTextField(
        blank=True,
        verbose_name="Currículo – Folha 1"
    )
    curriculo_folha_2 = RichTextField(
        blank=True,
        verbose_name="Currículo – Folha 2"
    )
    curriculo_pdf = models.FileField(
        upload_to="curriculo/pdf/",
        blank=True,
        null=True,
        verbose_name="Currículo – PDF"
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"


# ======================================================
# SERVIÇOS (CARDS)
# ======================================================
class ServiceCard(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="services"
    )

    titulo = models.CharField(max_length=100)
    descricao = RichTextField(verbose_name="Descrição")

    imagem = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    slug = models.SlugField()
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.titulo


# ======================================================
# PROJETOS (CARDS)
# ======================================================
class ProjectCard(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    titulo = models.CharField(max_length=150)
    descricao = RichTextField(verbose_name="Descrição")

    imagem = models.ImageField(upload_to="projects/")
    slug = models.SlugField()

    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return self.titulo


# ======================================================
# CONTATO
# ======================================================
class ContactContent(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        limit_choices_to={"slug": "contato"}
    )

    texto = RichTextField(verbose_name="Texto")
    email = models.EmailField()
    telefone = models.CharField(max_length=30)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contato"
