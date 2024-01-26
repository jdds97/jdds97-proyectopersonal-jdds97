from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .views import (
    CrearInstructor,
    ListarInstructores,
    EditarInstructor,
    EliminarInstructor,
    welcome,
)


urlpatterns = [
    # region welcome
    path("", welcome, name="welcome"),
    # endregion
    # region CRUD de Instructor
    path(
        "instructor/nuevo/",
        staff_member_required(login_required(CrearInstructor.as_view())),
        name="crear_instructor",
    ),
    path(
        "instructor/listado/",
        staff_member_required(login_required(ListarInstructores.as_view())),
        name="listar_instructors",
    ),
    path(
        "instructor/editar/<int:pk>",
        staff_member_required(login_required(EditarInstructor.as_view())),
        name="editar_instructor",
    ),
    path(
        "instructor/eliminar/<int:pk>",
        staff_member_required(login_required(EliminarInstructor.as_view())),
        name="eliminar_instructor",
    ),
    # endregion
]
