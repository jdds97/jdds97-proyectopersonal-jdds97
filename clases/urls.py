from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (
    CrearClase,
    ListarClases,
    EditarClase,
    EliminarClase,
    CrearTipoClase,
    ListarTipoClases,
    EditarTipoClase,
    EliminarTipoClase,
    CrearReserva,
    ListarReservas,
    EditarReserva,
    EliminarReserva,
    welcome,
)

urlpatterns = [
    # region welcome
    path("", welcome, name="welcome"),
    # region CRUD de Clases
    path(
        "nuevo/",
        staff_member_required(login_required(CrearClase.as_view())),
        name="crear_clase",
    ),
    path(
        "listado/",
        staff_member_required(login_required(ListarClases.as_view())),
        name="listar_clases",
    ),
    path(
        "editar/<int:pk>",
        staff_member_required(login_required(EditarClase.as_view())),
        name="editar_clase",
    ),
    path(
        "eliminar/<int:pk>",
        staff_member_required(login_required(EliminarClase.as_view())),
        name="eliminar_clase",
    ),
    # endregion
    # region CRUD de Tipo de Clases
    path(
        "tipo_clase/nuevo/",
        staff_member_required(login_required(CrearTipoClase.as_view())),
        name="crear_tipo_clase",
    ),
    path(
        "tipo_clase/listado/",
        staff_member_required(login_required(ListarTipoClases.as_view())),
        name="listar_tipo_clases",
    ),
    path(
        "tipo_clase/editar/<int:pk>",
        staff_member_required(login_required(EditarTipoClase.as_view())),
        name="editar_tipo_clase",
    ),
    path(
        "tipo_clase/eliminar/<int:pk>",
        staff_member_required(login_required(EliminarTipoClase.as_view())),
        name="eliminar_tipo_clase",
    ),
    # endregion
    # region CRUD de Clases
    path(
        "reserva/nuevo/",
        staff_member_required(login_required(CrearReserva.as_view())),
        name="crear_reserva",
    ),
    path(
        "reserva/listado/",
        staff_member_required(login_required(ListarReservas.as_view())),
        name="listar_reservas",
    ),
    path(
        "reserva/editar/<int:pk>",
        staff_member_required(login_required(EditarReserva.as_view())),
        name="editar_reserva",
    ),
    path(
        "reserva/eliminar/<int:pk>",
        staff_member_required(login_required(EliminarReserva.as_view())),
        name="eliminar_reserva",
    ),
    # endregion
]
