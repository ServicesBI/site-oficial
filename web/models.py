from django.db import models


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
        verbose_name="Página"
    )

    # ================= HERO / CONTEÚDO =================
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título principal"
    )

    subtitulo = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Subtítulo"
    )

    texto = models.TextField(
        blank=True,
        verbose_name="Texto principal"
    )

    banner_image = models.ImageField(
        upload_to="pages/banners/",
        blank=True,
        null=True,
        verbose_name="Banner da página"
    )

    # ================= CURRÍCULO (USADO APENAS NA PAGE curriculo) =================
    curriculo_folha_1 = models.TextField(
        blank=True,
        verbose_name="Currículo – Texto da Folha 1"
    )

    curriculo_folha_2 = models.TextField(
        blank=True,
        verbose_name="Currículo – Texto da Folha 2"
    )

    curriculo_pdf = models.FileField(
        upload_to="curriculo/pdf/",
        blank=True,
        null=True,
        verbose_name="Currículo – PDF"
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_slug_display()

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
        related_name="services",
        verbose_name="Página"
    )

    titulo = models.CharField(
        max_length=100,
        verbose_name="Título do serviço"
    )

    descricao = models.TextField(
        max_length=500,
        verbose_name="Descrição do serviço"
    )

    imagem = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True,
        verbose_name="Imagem do serviço"
    )

    slug = models.SlugField(
        verbose_name="Slug (link)"
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordem"
    )

    def __str__(self):
        return f"{self.titulo} ({self.page})"

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Serviço – Card"
        verbose_name_plural = "Serviços – Cards"


# ======================================================
# PROJETOS (CARDS)
# ======================================================
class ProjectCard(models.Model):
    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Página"
    )

    titulo = models.CharField(
        max_length=150,
        verbose_name="Título do projeto"
    )

    descricao = models.TextField(
        max_length=600,
        verbose_name="Descrição do projeto"
    )

    imagem = models.ImageField(
        upload_to="projects/",
        verbose_name="Imagem do projeto"
    )

    slug = models.SlugField(
        verbose_name="Slug"
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name="Ativo"
    )

    ordem = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordem"
    )

    def __str__(self):
        return f"{self.titulo} ({self.page})"

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Projeto – Card"
        verbose_name_plural = "Projetos – Cards"


# ======================================================
# CONTATO (SEM CARDS)
# ======================================================
class ContactContent(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        limit_choices_to={"slug": "contato"},
        verbose_name="Página"
    )

    texto = models.TextField(
        verbose_name="Texto de apresentação"
    )

    email = models.EmailField(
        verbose_name="E-mail"
    )

    telefone = models.CharField(
        max_length=30,
        verbose_name="Telefone"
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contato"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contato"


# ======================================================
# TEMA DA PÁGINA
# ======================================================
class PageTheme(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="theme",
        verbose_name="Página"
    )

    menu_color = models.CharField(max_length=7, default="#ffffff")

    title_color = models.CharField(max_length=7, default="#fde047")
    subtitle_color = models.CharField(max_length=7, default="#38bdf8")
    text_color = models.CharField(max_length=7, default="#e5e7eb")

    services_title_color = models.CharField(max_length=7, default="#fde047")
    services_text_color = models.CharField(max_length=7, default="#334155")
    services_border_color = models.CharField(max_length=7, default="#fde047")
    services_button_color = models.CharField(max_length=7, default="#fde047")

    projects_title_color = models.CharField(max_length=7, default="#fde047")
    projects_text_color = models.CharField(max_length=7, default="#334155")
    projects_border_color = models.CharField(max_length=7, default="#fde047")
    projects_button_color = models.CharField(max_length=7, default="#fde047")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tema – {self.page}"

    class Meta:
        verbose_name = "Tema da Página"
        verbose_name_plural = "Temas da Página"


