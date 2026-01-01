from django.db import models


# ======================================================
# PÁGINAS (BASE DE TUDO) — OPÇÃO A
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

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_slug_display()

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"


# ======================================================
# SERVIÇOS (CARDS — REUTILIZÁVEIS)
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
# PROJETOS (CARDS — REUTILIZÁVEIS)
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
# CURRÍCULO (ESPECIAL — SEM CARDS)
# ======================================================
class Curriculo(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        limit_choices_to={"slug": "curriculo"},
        verbose_name="Página",
        null=True,
        blank=True
    )

    texto_folha_1 = models.TextField(
        verbose_name="Texto da Folha 1"
    )

    texto_folha_2 = models.TextField(
        verbose_name="Texto da Folha 2"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última atualização"
    )

    def __str__(self):
        return "Currículo – ServicesBI"

    class Meta:
        verbose_name = "Currículo"
        verbose_name_plural = "Currículo"


# ======================================================
# CONTATO (SEM CARDS / PROJETOS)
# ======================================================
class ContactContent(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        limit_choices_to={"slug": "contato"},
        verbose_name="Página",
        null=True,
        blank=True
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
        return "Contato – Conteúdo"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contato"


# ======================================================
# TEMA DA PÁGINA (APARÊNCIA — 1 PRA 1 COM PAGE)
# ======================================================
class PageTheme(models.Model):
    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        related_name="theme",
        verbose_name="Página"
    )

    # ================= MENU =================
    menu_color = models.CharField(
        max_length=7,
        default="#ffffff",
        verbose_name="Cor do menu"
    )

    # ================= HERO =================
    title_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Cor do título"
    )

    subtitle_color = models.CharField(
        max_length=7,
        default="#38bdf8",
        verbose_name="Cor do subtítulo"
    )

    text_color = models.CharField(
        max_length=7,
        default="#e5e7eb",
        verbose_name="Cor do texto"
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

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tema – {self.page}"

    class Meta:
        verbose_name = "Tema da Página"
        verbose_name_plural = "Temas da Página"

# ======================================================
# PROXY MODELS — ADMIN POR PÁGINA (CMS STYLE)
# ======================================================

class HomePage(Page):
    class Meta:
        proxy = True
        verbose_name = "Home"
        verbose_name_plural = "Home"


class PythonPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Python"
        verbose_name_plural = "Python"


class PowerBIPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Power BI"
        verbose_name_plural = "Power BI"


class AutomacoesPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Automações"
        verbose_name_plural = "Automações"


class ExcelPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Excel"
        verbose_name_plural = "Excel"


class CurriculoPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Currículo"
        verbose_name_plural = "Currículo"


class ContatoPage(Page):
    class Meta:
        proxy = True
        verbose_name = "Contato"
        verbose_name_plural = "Contato"


