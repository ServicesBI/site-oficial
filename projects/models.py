from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Título'
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Slug'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Descrição'
    )

    image = models.ImageField(
        upload_to='projects/',
        verbose_name='Imagem de capa'
    )

    project_url = models.URLField(
        blank=True,
        verbose_name='Link do projeto'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordem'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
