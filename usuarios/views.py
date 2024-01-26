from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Instructor, Cliente

""" 


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado con exito")
            return redirect("usuarios:login")

        messages.error(request, "Error al registrar")
    else:
        form = RegisterForm()
    return render(request, "usuarios/register.html"{"form":form}) """


# region welcome
def welcome(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, "usuarios/index.html", {})


# endregion
# region  CRUD de Instructor
class CrearInstructor(CreateView):
    """
    Vista para crear un instructor.
    """

    model = Instructor
    fields = "__all__"
    success_url = reverse_lazy("listar_instructores")


class ListarInstructores(ListView):
    """
    Vista para listar los instructores.
    """

    model = Instructor


class EditarInstructor(UpdateView):
    """
    Vista para editar un instructor.
    """

    model = Instructor
    fields = "__all__"
    success_url = reverse_lazy("listar_instructores")


class EliminarInstructor(DeleteView):
    """
    Vista para eliminar un instructor.
    """

    model = Instructor
    success_url = reverse_lazy("listar_instructores")


# endregion
