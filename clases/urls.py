from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .views import (
    CrearClase,
    ListarClases,
    EditarClase,
    DetalleClase,
    EliminarClase,
    ClasesClientes,
    ClasesPorTipo,
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
    # detalle clase
    path(
        "detalle/<int:pk>",
        login_required(DetalleClase.as_view()),
        name="detalle_clase",
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
    # region Clases tipo
    path(
        "<str:username>/",
        login_required(ClasesClientes.as_view()),
        name="clases_cliente",
    ),
    # clases por tipo
    path(
        "tipo/",
        login_required(ClasesPorTipo.as_view()),
        name="clases_por_tipo",
    ),
    # endregion
]
