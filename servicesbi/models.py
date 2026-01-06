from django.db import models
from ckeditor.fields import RichTextField


# ======================================================
# PAGE (BASE PARA TODAS AS PÁGINAS)
# ======================================================
class Page(models.Model):
    """
    Representa uma página do site:
    home, python, powerbi, automacoes, excel, curriculo, contato
    """

    SLUG_CHOICES = [
        ("home", "Home"),
        ("python", "Python"),
        ("powerbi", "Power BI"),
        ("automacoes", "Automações"),
        ("excel", "Excel"),
        ("curriculo", "Currículo"),
        ("contato", "Contato"),
    ]

    slug = models.CharField(
        max_length=50,
        choices=SLUG_CHOICES,
        unique=True
    )

    # =========================
    # BANNER (JÁ EXISTENTES)
    # =========================
    banner_title = models.CharField(
        max_length=255,
        verbose_name="Título do Banner"
    )

    banner_subtitle = models.CharField(
        max_length=255,
        verbose_name="Subtítulo do Banner",
        blank=True
    )

    # =========================
    # 🔽 NOVOS CAMPOS DO BANNER
    # =========================
    banner_eyebrow = models.CharField(
        max_length=100,
        verbose_name="Texto superior do Banner",
        blank=True
    )

    banner_description = RichTextField(
        verbose_name="Descrição do Banner",
        blank=True
    )
    # =========================
    # 🔼 FIM DOS NOVOS CAMPOS
    # =========================

    def __str__(self):
        return self.get_slug_display()


# ======================================================
# SERVICE CARD (CARDS DE SERVIÇO)
# ======================================================
class ServiceCard(models.Model):
    """
    Cards de serviços exibidos nas páginas
    """

    page = models.ForeignKey(
        Page,
        related_name="services",
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=150,
        verbose_name="Título do Serviço"
    )

    description = RichTextField(
        verbose_name="Descrição do Serviço"
    )

    icon = models.ImageField(
        upload_to="services/icons/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page} - {self.title}"


# ======================================================
# PROJECT (PROJETOS)
# ======================================================
class Project(models.Model):
    """
    Projetos exibidos por página
    """

    page = models.ForeignKey(
        Page,
        related_name="projects",
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=150,
        verbose_name="Título do Projeto"
    )

    description = RichTextField(
        verbose_name="Descrição do Projeto"
    )

    image = models.ImageField(
        upload_to="projects/images/"
    )

    link = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page} - {self.title}"


# ======================================================
# CURRÍCULO (TEXTO DAS FOLHAS)
# ======================================================
class CurriculoSection(models.Model):
    """
    Texto do currículo (folha 1 e folha 2)
    """

    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        limit_choices_to={"slug": "curriculo"}
    )

    folha_1 = RichTextField(verbose_name="Folha 1")
    folha_2 = RichTextField(verbose_name="Folha 2")

    def __str__(self):
        return "Currículo"


# ======================================================
# CONTATO (TEXTOS AUXILIARES)
# ======================================================
class ContatoText(models.Model):
    """
    Textos auxiliares da página de contato
    """

    page = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        limit_choices_to={"slug": "contato"}
    )

    intro_text = RichTextField(
        verbose_name="Texto introdutório"
    )

    form_title = models.CharField(
        max_length=150,
        verbose_name="Título do Formulário"
    )

    def __str__(self):
        return "Contato"
