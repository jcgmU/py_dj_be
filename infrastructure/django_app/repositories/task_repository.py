# Importamos tipos para anotaciones de tipo en Python
from typing import List, Optional

# Importamos la entidad de tarea que define nuestro dominio
from domain.entities.task_entity import TaskEntity

# Importamos la interfaz que define los métodos que debe implementar el repositorio
from interface_adapters.repositories.i_task_repository import ITaskRepository

# Importamos el modelo de Django que representa la tabla en la base de datos
from infrastructure.django_app.models import TaskModel


# Definimos la clase que implementa la interfaz ITaskRepository
class TaskRepositoryDjango(ITaskRepository):

    def find_all(self) -> List[TaskEntity]:
        # Obtiene todos los registros ordenados por fecha de creación descendente
        task_models = TaskModel.objects.all().order_by("-created_at")
        # Convierte cada modelo de Django en una entidad de dominio
        task_entities = [
            TaskEntity(
                id=tm.id,
                title=tm.title,
                description=tm.description,
                completed=tm.completed,
                created_at=tm.created_at,
            )
            for tm in task_models
        ]
        return task_entities

    def find_by_id(self, task_id: int) -> Optional[TaskEntity]:
        try:
            # Intenta encontrar la tarea por su ID
            tm = TaskModel.objects.get(id=task_id)
            # Si la encuentra, la convierte en una entidad
            return TaskEntity(
                id=tm.id,
                title=tm.title,
                description=tm.description,
                completed=tm.completed,
                created_at=tm.created_at,
            )
        except TaskModel.DoesNotExist:
            # Si no encuentra la tarea, devuelve None
            return None

    def save(self, task: TaskEntity) -> TaskEntity:
        if task.id:
            # Si tiene ID, actualiza la tarea existente
            tm = TaskModel.objects.get(id=task.id)
            tm.title = task.title
            tm.description = task.description
            tm.completed = task.completed
            tm.save()
        else:
            # Si no tiene ID, crea una nueva tarea
            tm = TaskModel.objects.create(
                title=task.title, description=task.description, completed=task.completed
            )
        # Devuelve la entidad actualizada con todos sus datos
        return TaskEntity(
            id=tm.id,
            title=tm.title,
            description=tm.description,
            completed=tm.completed,
            created_at=tm.created_at,
        )

    def delete(self, task_id: int) -> bool:
        try:
            # Intenta encontrar y eliminar la tarea
            tm = TaskModel.objects.get(id=task_id)
            tm.delete()
            return True
        except TaskModel.DoesNotExist:
            # Si no existe la tarea, devuelve False
            return False
