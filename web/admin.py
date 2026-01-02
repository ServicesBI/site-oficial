from django.contrib import admin
from django import forms

from .models import (
    Page,
    PageTheme,
    ServiceCard,
    ProjectCard,
    ContactContent,
)

# ======================================================
# WIDGET DE COR (HEX + PICKER)
# ======================================================
class ColorHexWidget(forms.TextInput):
    input_type = "color"


# ======================================================
# FORM PRINCIPAL DA PAGE (COM TEMA INTEGRADO)
# ======================================================
class PageAdminForm(forms.ModelForm):
    # ===== HERO =====
    title_color = forms.CharField(widget=ColorHexWidget, required=False)
    subtitle_color = forms.CharField(widget=ColorHexWidget, required=False)
    text_color = forms.CharField(widget=ColorHexWidget, required=False)

    # ===== SERVIÇOS =====
    services_title_color = forms.CharField(widget=ColorHexWidget, required=False)
    services_text_color = forms.CharField(widget=ColorHexWidget, required=False)
    services_border_color = forms.CharField(widget=ColorHexWidget, required=False)
    services_button_color = forms.CharField(widget=ColorHexWidget, required=False)

    # ===== PROJETOS =====
    projects_title_color = forms.CharField(widget=ColorHexWidget, required=False)
    projects_text_color = forms.CharField(widget=ColorHexWidget, required=False)
    projects_border_color = forms.CharField(widget=ColorHexWidget, required=False)
    projects_button_color = forms.CharField(widget=ColorHexWidget, required=False)

    class Meta:
        model = Page
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            theme, _ = PageTheme.objects.get_or_create(page=self.instance)

            for field in [
                "title_color",
                "subtitle_color",
                "text_color",
                "services_title_color",
                "services_text_color",
                "services_border_color",
                "services_button_color",
                "projects_title_color",
                "projects_text_color",
                "projects_border_color",
                "projects_button_color",
            ]:
                self.fields[field].initial = getattr(theme, field)

    def save(self, commit=True):
        page = super().save(commit)
        theme, _ = PageTheme.objects.get_or_create(page=page)

        for field in self.cleaned_data:
            if hasattr(theme, field):
                setattr(theme, field, self.cleaned_data[field])

        theme.save()
        return page


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
# ADMIN BASE
# ======================================================
class BasePageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    list_display = ("titulo",)
    inlines = [ServiceCardInline, ProjectCardInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(slug=self.slug_fixo)

    def has_add_permission(self, request):
        return False

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ("Hero", {
                "fields": (
                    ("titulo", "title_color"),
                    ("subtitulo", "subtitle_color"),
                    ("texto", "text_color"),
                )
            }),
            ("Banner", {
                "fields": ("banner_image",)
            }),
            ("Serviços – Cores", {
                "fields": (
                    "services_title_color",
                    "services_text_color",
                    "services_border_color",
                    "services_button_color",
                )
            }),
            ("Projetos – Cores", {
                "fields": (
                    "projects_title_color",
                    "projects_text_color",
                    "projects_border_color",
                    "projects_button_color",
                )
            }),
        ]

        if obj and obj.slug == "curriculo":
            fieldsets.append(
                ("Currículo", {
                    "fields": (
                        "curriculo_folha_1",
                        "curriculo_folha_2",
                        "curriculo_pdf",
                    )
                })
            )

        return fieldsets


# ======================================================
# PROXIES (MENU)
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


@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):
    list_display = ("email", "telefone", "updated_at")
