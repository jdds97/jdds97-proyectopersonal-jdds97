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
from .models import Clase, TipoClase, Reserva


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
# region CRUD de Tipo de Clases


class CrearTipoClase(CreateView):
    """
    Vista para crear un tipo de clase.
    """

    model = TipoClase
    fields = "__all__"
    success_url = reverse_lazy("listar_tipo_clases")


class ListarTipoClases(ListView):
    """
    Vista para listar los tipos de clases.
    """

    model = TipoClase


class EditarTipoClase(UpdateView):
    """
    Vista para editar un tipo de clase.
    """

    model = TipoClase
    fields = "__all__"
    success_url = reverse_lazy("listar_tipo_clases")


class EliminarTipoClase(DeleteView):
    """
    Vista para eliminar un tipo de clase.
    """

    model = TipoClase
    success_url = reverse_lazy("listar_tipo_clases")


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
