# from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from .models import Clase, Reserva


# pylint: disable=no-member
# region welcome
def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, "clases/index.html", {})


# endregion


# region CRUD de Clases
class CrearClase(CreateView):
    """
    Vista para crear una clase.
    """

    model = Clase
    fields = "__all__"
    success_url = reverse_lazy("listar_clases")


class ListarClases(ListView):
    """
    Vista para listar las clases.
    """

    model = Clase


class EditarClase(UpdateView):
    """
    Vista para editar una clase.
    """

    model = Clase
    template_name_suffix = "_update_form"
    fields = "__all__"
    success_url = reverse_lazy("listar_clases")


class EliminarClase(DeleteView):
    """
    Vista para eliminar una clase.
    """

    model = Clase
    success_url = reverse_lazy("listar_clases")


class DetalleClase(DetailView):
    """
    Vista para ver los detalles de una clase.
    """

    model = Clase
    success_url = reverse_lazy("listar_clases")


# endregion


# region CRUD de Reservas
class CrearReserva(CreateView):
    """
    Vista para crear una reserva.
    """

    model = Reserva
    fields = "__all__"
    success_url = reverse_lazy("listar_reservas")
    


class ListarReservas(ListView):
    """
    Vista para listar las reservas.
    """

    model = Reserva


class EditarReserva(UpdateView):
    """
    Vista para editar una reserva.
    """

    model = Reserva
    fields = "__all__"
    success_url = reverse_lazy("listar_reservas")


class EliminarReserva(DeleteView):
    """
    Vista para eliminar una reserva.
    """

    model = Reserva
    success_url = reverse_lazy("listar_reservas")


# endregion
# region Clases tipo
class ClasesClientes(ListView):
    """
    Vista para listar las clases para los clientes.
    """

    model = Clase
    template_name_suffix = "_clientes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clases_clientes"] = Clase.objects.filter(
            cupos_disponibles__gt=0, usuarios__username=self.request.user.username
        )
        return context


class ClasesPorTipo(ListView):
    """
    Vista para listar las clases por tipo.
    """

    model = Clase
    template_name_suffix = "_por_tipo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clases_tipo"] = Clase.objects.filter(
            tipo_clase__nombre=self.kwargs["tipo_clase"]
        )
        return context
