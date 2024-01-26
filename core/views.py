from django.shortcuts import render
from django.views.generic import ListView


def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, "core/index.html", {})
