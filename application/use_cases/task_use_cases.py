# Este archivo contiene las acciones que se pueden hacer con las tareas
from domain.entities.task_entity import TaskEntity  # Importamos el "molde" de tareas


class TaskUseCases:
    def __init__(self, task_repository):
        # Cuando creamos esta clase, le damos un "repositorio"
        # (algo que sabe guardar y buscar tareas)
        self.task_repository = task_repository

    def create_task(self, title: str, description: str) -> TaskEntity:
        # Esta función CREA una nueva tarea
        # 1. Preparamos la tarea con título y descripción
        # 2. La marcamos como "no completada" (completed=False)
        # 3. No ponemos ID porque la base de datos lo asignará
        new_task = TaskEntity(
            id=None, title=title, description=description, completed=False
        )
        # Guardamos la tarea y devolvemos la versión guardada (que ya tendrá ID)
        saved_task = self.task_repository.save(new_task)
        return saved_task

    def get_all_tasks(self):
        # Esta función OBTIENE TODAS las tareas
        # Simplemente le pedimos al repositorio que nos dé todas
        return self.task_repository.find_all()

    def get_task_by_id(self, task_id: int):
        # Esta función BUSCA UNA tarea específica por su número ID
        return self.task_repository.find_by_id(task_id)

    def update_task(self, task_id: int, title: str, description: str, completed: bool):
        # Esta función ACTUALIZA una tarea existente
        # 1. Primero buscamos si la tarea existe
        existing_task = self.task_repository.find_by_id(task_id)

        # 2. Si no existe, devolvemos None (nada)
        if not existing_task:
            return None

        # 3. Si existe, actualizamos sus datos
        existing_task.title = title
        existing_task.description = description
        existing_task.completed = completed

        # 4. Guardamos los cambios y devolvemos la tarea actualizada
        return self.task_repository.save(existing_task)

    def delete_task(self, task_id: int) -> bool:
        # Esta función ELIMINA una tarea
        # Devuelve True si se borró correctamente, False si no existía
        return self.task_repository.delete(task_id)
