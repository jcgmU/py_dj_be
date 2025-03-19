# Importamos lo necesario para trabajar
from typing import List, Optional
from domain.entities.task_entity import TaskEntity
from interface_adapters.repositories.i_task_repository import ITaskRepository
from infrastructure.django_app.models import TaskModel


# Esta clase es la que realmente hace el trabajo de guardar y recuperar tareas
class TaskRepositoryDjango(ITaskRepository):  # "Firma" el contrato ITaskRepository

    def find_all(self) -> List[TaskEntity]:
        # FUNCIÓN: Busca TODAS las tareas
        # 1. Pide a Django todas las tareas ordenadas por fecha (más nuevas primero)
        task_models = TaskModel.objects.all().order_by("-created_at")

        # 2. Convierte cada tarea de "formato Django" a "formato de nuestra app"
        task_entities = [
            TaskEntity(
                id=tm.id,  # Copia el ID
                title=tm.title,  # Copia el título
                description=tm.description,  # Copia la descripción
                completed=tm.completed,  # Copia si está completada
                created_at=tm.created_at,  # Copia la fecha de creación
            )
            for tm in task_models  # Hace esto para cada tarea encontrada
        ]
        # 3. Devuelve la lista convertida
        return task_entities

    def find_by_id(self, task_id: int) -> Optional[TaskEntity]:
        # FUNCIÓN: Busca UNA tarea específica
        try:
            # 1. Intenta encontrar la tarea con ese ID
            tm = TaskModel.objects.get(id=task_id)

            # 2. Si la encuentra, la convierte al formato de nuestra app
            return TaskEntity(
                id=tm.id,
                title=tm.title,
                description=tm.description,
                completed=tm.completed,
                created_at=tm.created_at,
            )
        except TaskModel.DoesNotExist:
            # 3. Si no existe esa tarea, devuelve None (nada)
            return None

    def save(self, task: TaskEntity) -> TaskEntity:
        # FUNCIÓN: Guarda una tarea (nueva o actualizada)
        if task.id:
            # 1A. Si tiene ID, es una tarea que ya existe → ACTUALIZAR
            tm = TaskModel.objects.get(id=task.id)  # Busca la original
            tm.title = task.title  # Actualiza título
            tm.description = task.description  # Actualiza descripción
            tm.completed = task.completed  # Actualiza estado
            tm.save()  # Guarda cambios
        else:
            # 1B. Si NO tiene ID, es una tarea nueva → CREAR
            tm = TaskModel.objects.create(  # Crea nueva tarea
                title=task.title, description=task.description, completed=task.completed
            )

        # 2. Devuelve la tarea guardada (con ID asignado y fechas)
        return TaskEntity(
            id=tm.id,
            title=tm.title,
            description=tm.description,
            completed=tm.completed,
            created_at=tm.created_at,
        )

    def delete(self, task_id: int) -> bool:
        # FUNCIÓN: Elimina una tarea
        try:
            # 1. Intenta encontrar la tarea
            tm = TaskModel.objects.get(id=task_id)
            # 2. Si existe, la elimina
            tm.delete()
            # 3. Informa que todo salió bien
            return True
        except TaskModel.DoesNotExist:
            # 4. Si no existe, informa que no se pudo borrar
            return False
