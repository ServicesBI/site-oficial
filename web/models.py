from django.db import models

class Curriculo(models.Model):
    titulo_banner = models.CharField(max_length=200)
    subtitulo_banner = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to="curriculo/banner/", blank=True, null=True)
    texto_folha_1 = models.TextField()
    texto_folha_2 = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Currículo - ServicesBI"
