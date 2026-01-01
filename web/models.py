from django.db import models


# =========================
# CURRÍCULO
# =========================
class Curriculo(models.Model):
    titulo_banner = models.CharField(
        max_length=200,
        verbose_name="Título do Banner"
    )

    subtitulo_banner = models.CharField(
        max_length=200,
        verbose_name="Subtítulo do Banner"
    )

    banner_image = models.ImageField(
        upload_to="curriculo/banner/",
        blank=True,
        null=True,
        verbose_name="Imagem do Banner"
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
        return "Currículo - ServicesBI"

    class Meta:
        verbose_name = "Currículo"
        verbose_name_plural = "Currículos"


# =========================
# TEMA DO SITE
# =========================
class SiteTheme(models.Model):
    PAGE_CHOICES = [
        ("global", "Global"),
        ("home", "Home"),
        ("python", "Python"),
        ("powerbi", "Power BI"),
        ("automacoes", "Automações"),
        ("excel", "Excel"),
        ("curriculo", "Currículo"),
        ("contato", "Contato"),
    ]

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome do Tema"
    )

    pagina = models.CharField(
        max_length=20,
        choices=PAGE_CHOICES,
        default="global",
        verbose_name="Página"
    )

    # ================= MENU =================
    menu_color = models.CharField(
        max_length=7,
        default="#ffffff",
        verbose_name="Cor do menu",
        help_text="Cor dos links do menu"
    )

    # ================= HERO / BANNER =================
    hero_title_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Cor do título principal",
        help_text="Título principal do banner"
    )

    hero_subtitle_color = models.CharField(
        max_length=7,
        default="#38bdf8",
        verbose_name="Cor do subtítulo",
        help_text="Subtítulo do banner"
    )

    # ================= SERVIÇOS =================
    services_title_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Serviços - Cor do título"
    )

    services_text_color = models.CharField(
        max_length=7,
        default="#334155",
        verbose_name="Serviços - Cor da descrição"
    )

    services_border_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Serviços - Cor da borda"
    )

    services_button_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Serviços - Cor do botão"
    )

    # ================= PROJETOS =================
    projects_title_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Projetos - Cor do título"
    )

    projects_text_color = models.CharField(
        max_length=7,
        default="#334155",
        verbose_name="Projetos - Cor da descrição"
    )

    projects_border_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Projetos - Cor da borda"
    )

    projects_button_color = models.CharField(
        max_length=7,
        default="#fde047",
        verbose_name="Projetos - Cor do botão"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última atualização"
    )

    def __str__(self):
        return f"{self.nome} ({self.get_pagina_display()})"

    class Meta:
        verbose_name = "Tema do Site"
        verbose_name_plural = "Temas do Site"
