from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from fitness.models import Rutina
from clases.models import Clase


class Cliente(AbstractUser):
    rutina_asignada = models.ForeignKey(
        Rutina, on_delete=models.SET_NULL, null=True, blank=True
    )
    clases_apuntadas = models.ManyToManyField(
        Clase, blank=True, related_name="clientes"
    )
    groups = models.ManyToManyField(Group, blank=True, related_name="clientes_groups")
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="clientes_user_permissions"
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"


class Instructor(AbstractUser):
    clases_asignadas = models.ForeignKey(
        Clase,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        related_name="clase_asignadas",
    )
    groups = models.ManyToManyField(
        Group, blank=True, related_name="instructors_groups"
    )
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="instructores_user_permissions"
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = "Instructores"
        verbose_name = "Instructor"


class Staff(AbstractUser):
    is_staff = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="staffs_groups")
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="staffs_user_permissions"
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = "Staffs"
        verbose_name = "Staff"


class Admin(AbstractUser):
    is_superuser = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="admins_groups")
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="admins_user_permissions"
    )

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = "Admins"
        verbose_name = "Admin"
