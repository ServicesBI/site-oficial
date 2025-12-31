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
    nome = models.CharField(
        max_length=100,
        default="Tema Principal",
        verbose_name="Nome do Tema"
    )

    cor_titulo = models.CharField(
        max_length=7,
        default="#ffffff",
        help_text="Cor dos títulos principais (ex: #ffffff)",
        verbose_name="Cor do Título"
    )

    cor_subtitulo = models.CharField(
        max_length=7,
        default="#38bdf8",
        help_text="Cor dos subtítulos (ex: #38bdf8)",
        verbose_name="Cor do Subtítulo"
    )

    cor_texto = models.CharField(
        max_length=7,
        default="#e5e7eb",
        help_text="Cor do texto padrão (ex: #e5e7eb)",
        verbose_name="Cor do Texto"
    )

    cor_botao = models.CharField(
        max_length=7,
        default="#38bdf8",
        help_text="Cor principal dos botões (ex: #38bdf8)",
        verbose_name="Cor do Botão"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última atualização"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tema do Site"
        verbose_name_plural = "Temas do Site"
