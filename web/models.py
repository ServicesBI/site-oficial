from django.db import models


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

    nome = models.CharField(max_length=100)
    pagina = models.CharField(
        max_length=20,
        choices=PAGE_CHOICES,
        default="global"
    )

    cor_titulo = models.CharField(
        max_length=7,
        default="#ffffff",
        help_text="Cor dos títulos principais"
    )

    cor_subtitulo = models.CharField(
        max_length=7,
        default="#38bdf8",
        help_text="Cor dos subtítulos"
    )

    cor_texto = models.CharField(
        max_length=7,
        default="#e5e7eb",
        help_text="Cor do texto padrão"
    )

    cor_botao = models.CharField(
        max_length=7,
        default="#38bdf8",
        help_text="Cor principal dos botões"
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.get_pagina_display()})"


    class Meta:
        verbose_name = "Tema do Site"
        verbose_name_plural = "Temas do Site"
