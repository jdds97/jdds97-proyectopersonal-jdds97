from django.db import models


class TipoClase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.nombre)


class Clase(models.Model):
    tramo = models.PositiveIntegerField(default=0)
    tipo_clase = models.ForeignKey(
        TipoClase,
        on_delete=models.CASCADE,
    )
    instructor = models.OneToOneField(
        "usuarios.Instructor", on_delete=models.CASCADE, default=None
    )
    cupos_disponibles = models.PositiveIntegerField(default=0)
    usuarios = models.ManyToManyField(
        "usuarios.Cliente",
    )

    def __str__(self):
        return f"Clase - {self.tipo_clase}"


class Reserva(models.Model):
    usuario = models.ForeignKey("usuarios.Cliente", on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva - {self.usuario} - {self.clase} - {self.fecha_reserva}"
