# Importamos las herramientas de Django para crear modelos (tablas) en la base de datos
from django.db import models


# Definimos la estructura de la tabla "TaskModel" en la base de datos
class TaskModel(models.Model):
    # Campo para el TÍTULO de la tarea (texto corto, máximo 255 caracteres)
    title = models.CharField(max_length=255)

    # Campo para la DESCRIPCIÓN de la tarea (texto largo sin límite)
    description = models.TextField()

    # Campo para saber si está COMPLETADA (sí/no), por defecto "no" (False)
    completed = models.BooleanField(default=False)

    # Campo para la FECHA DE CREACIÓN, se llena automáticamente al crear la tarea
    created_at = models.DateTimeField(auto_now_add=True)

    # Esta función define cómo se muestra cada tarea cuando la imprimimos
    # Por ejemplo, al verla en el panel de administración de Django
    def __str__(self):
        return self.title
