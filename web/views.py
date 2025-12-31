from django.shortcuts import render
from projects.models import Project


def home(request):
    return render(request, "web/home.html")


def python(request):
    projects = Project.objects.filter(
        page='python',
        is_active=True
    ).order_by('order')

    return render(request, "web/python.html", {
        'projects': projects
    })


def powerbi(request):
    projects = Project.objects.filter(
        page='powerbi',
        is_active=True
    ).order_by('order')

    return render(request, "web/powerbi.html", {
        'projects': projects
    })


def automacoes(request):
    projects = Project.objects.filter(
        page='automacoes',
        is_active=True
    ).order_by('order')

    return render(request, "web/automacoes.html", {
        'projects': projects
    })


def excel(request):
    projects = Project.objects.filter(
        page='excel',
        is_active=True
    ).order_by('order')

    return render(request, "web/excel.html", {
        'projects': projects
    })


def curriculo(request):
    return render(request, "web/curriculo.html")


def contato(request):
    return render(request, "web/contato.html")
