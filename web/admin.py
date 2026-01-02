from django.contrib import admin
from django import forms

from .models import (
    Page,
    ServiceCard,
    ProjectCard,
)

# ======================================================
# WIDGET DE COR (HEX + PICKER NO MESMO INPUT)
# ======================================================
class ColorHexWidget(forms.TextInput):
    template_name = "admin/widgets/color_hex.html"

    class Media:
        js = ("admin/js/color_sync.js",)



# ======================================================
# INLINES
# ======================================================
class ServiceCardInline(admin.TabularInline):
    model = ServiceCard
    extra = 0
    ordering = ("ordem",)
    prepopulated_fields = {"slug": ("titulo",)}


class ProjectCardInline(admin.TabularInline):
    model = ProjectCard
    extra = 0
    ordering = ("ordem",)
    prepopulated_fields = {"slug": ("titulo",)}


# ======================================================
# ADMIN BASE (COM CAMPOS NA MESMA LINHA)
# ======================================================
class BasePageAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    inlines = [ServiceCardInline, ProjectCardInline]

    fieldsets = (
        ("Hero", {
            "fields": (
                ("titulo", "titulo_color"),
                ("subtitulo", "subtitulo_color"),
                ("texto", "texto_color"),
            )
        }),
        ("Banner", {
            "fields": ("banner_image",)
        }),
        ("Serviços – Cores", {
            "fields": (
                ("services_title_color", "services_text_color"),
                ("services_border_color", "services_button_color"),
            )
        }),
        ("Projetos – Cores", {
            "fields": (
                ("projects_title_color", "projects_text_color"),
                ("projects_border_color", "projects_button_color"),
            )
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(slug=self.slug_fixo)

    def has_add_permission(self, request):
        # pode deixar True enquanto cria as páginas
        return True

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        color_fields = [
            "titulo_color",
            "subtitulo_color",
            "texto_color",
            "services_title_color",
            "services_text_color",
            "services_border_color",
            "services_button_color",
            "projects_title_color",
            "projects_text_color",
            "projects_border_color",
            "projects_button_color",
        ]

        for field in color_fields:
            if field in form.base_fields:
                form.base_fields[field].widget = ColorHexWidget()

        return form


# ======================================================
# PROXIES (MENU DO ADMIN)
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


# ======================================================
# REGISTROS
# ======================================================
@admin.register(HomePage)
class HomeAdmin(BasePageAdmin):
    slug_fixo = "home"


@admin.register(PythonPage)
class PythonAdmin(BasePageAdmin):
    slug_fixo = "python"


@admin.register(PowerBIPage)
class PowerBIAdmin(BasePageAdmin):
    slug_fixo = "powerbi"


@admin.register(AutomacoesPage)
class AutomacoesAdmin(BasePageAdmin):
    slug_fixo = "automacoes"


@admin.register(ExcelPage)
class ExcelAdmin(BasePageAdmin):
    slug_fixo = "excel"


@admin.register(CurriculoPage)
class CurriculoAdmin(BasePageAdmin):
    slug_fixo = "curriculo"
