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

    # ================= HERO =================
    titulo = models.CharField(max_length=200, verbose_name="Título principal")
    titulo_color = models.CharField(max_length=7, default="#ffffff", verbose_name="Cor do título")

    subtitulo = models.CharField(max_length=300, blank=True, verbose_name="Subtítulo")
    subtitulo_color = models.CharField(max_length=7, default="#cbd5e1", verbose_name="Cor do subtítulo")

    texto = models.TextField(blank=True, verbose_name="Texto principal")
    texto_color = models.CharField(max_length=7, default="#e5e7eb", verbose_name="Cor do texto")

    banner_image = models.ImageField(
        upload_to="pages/banners/",
        blank=True,
        null=True,
        verbose_name="Banner da página"
    )

    # ================= SERVIÇOS =================
    services_title_color = models.CharField(max_length=7, default="#fde047", verbose_name="Serviços – Título")
    services_text_color = models.CharField(max_length=7, default="#334155", verbose_name="Serviços – Texto")
    services_border_color = models.CharField(max_length=7, default="#fde047", verbose_name="Serviços – Borda")
    services_button_color = models.CharField(max_length=7, default="#fde047", verbose_name="Serviços – Botão")

    # ================= PROJETOS =================
    projects_title_color = models.CharField(max_length=7, default="#fde047", verbose_name="Projetos – Título")
    projects_text_color = models.CharField(max_length=7, default="#334155", verbose_name="Projetos – Texto")
    projects_border_color = models.CharField(max_length=7, default="#fde047", verbose_name="Projetos – Borda")
    projects_button_color = models.CharField(max_length=7, default="#fde047", verbose_name="Projetos – Botão")

    # ================= CURRÍCULO =================
    curriculo_folha_1 = models.TextField(blank=True, verbose_name="Currículo – Folha 1")
    curriculo_folha_2 = models.TextField(blank=True, verbose_name="Currículo – Folha 2")
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
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="services")

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)

    imagem = models.ImageField(upload_to="services/", blank=True, null=True)

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
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="projects")

    titulo = models.CharField(max_length=150)
    descricao = models.TextField(max_length=600)
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
    page = models.OneToOneField(Page, on_delete=models.CASCADE, limit_choices_to={"slug": "contato"})

    texto = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=30)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contato"
