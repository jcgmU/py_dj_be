# Este archivo define cómo es una "tarea" en nuestra aplicación
from dataclasses import dataclass  # Ayuda a crear clases más simples
from typing import Optional  # Para marcar campos que pueden ser vacíos
from datetime import datetime  # Para manejar fechas y horas


@dataclass  # Esta etiqueta simplifica la clase
class TaskEntity:  # Define la estructura de una tarea
    # Estos son los datos que tiene cada tarea:
    id: Optional[int]  # Número de identificación (puede ser vacío)
    title: str  # Título de la tarea (texto)
    description: str  # Descripción detallada (texto largo)
    completed: bool  # Estado: completada o no (verdadero/falso)
    created_at: Optional[datetime] = None  # Fecha de creación (puede ser vacía)

    # Esta función construye una nueva tarea:
    def __init__(
        self,
        id: Optional[int],  # ID puede ser None para tareas nuevas
        title: str,  # Título siempre es necesario
        description: str,  # Descripción siempre es necesaria
        completed: bool = False,  # Por defecto, la tarea no está completada
        created_at: Optional[datetime] = None,  # Fecha puede ser asignada después
    ):
        # Guarda todos los datos en la tarea
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at
