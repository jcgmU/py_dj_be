# application/use_cases/task_use_cases.py
from domain.entities.task_entity import TaskEntity


class TaskUseCases:
    def __init__(self, task_repository):
        # El constructor recibe un repositorio como dependencia
        # Esto permite la inversión de dependencias (principio SOLID)
        self.task_repository = task_repository

    def create_task(self, title: str, description: str) -> TaskEntity:
        # Crea una nueva tarea con los datos básicos
        # El ID es None porque será asignado por la base de datos
        # completed se inicializa como False por defecto
        new_task = TaskEntity(
            id=None, title=title, description=description, completed=False
        )
        # Guardar en el repositorio (BD)
        saved_task = self.task_repository.save(new_task)
        return saved_task

    def get_all_tasks(self):
        # Obtiene todas las tareas del repositorio
        return self.task_repository.find_all()

    def get_task_by_id(self, task_id: int):
        # Busca una tarea específica por su ID
        return self.task_repository.find_by_id(task_id)

    def update_task(self, task_id: int, title: str, description: str, completed: bool):
        # Primero verifica si la tarea existe
        existing_task = self.task_repository.find_by_id(task_id)
        if not existing_task:
            # Si no existe, retorna None
            return None

        # Actualiza los campos de la tarea existente
        existing_task.title = title
        existing_task.description = description
        existing_task.completed = completed
        # Guarda los cambios en el repositorio
        return self.task_repository.save(existing_task)

    def delete_task(self, task_id: int) -> bool:
        # Elimina una tarea por su ID
        # Retorna True si se eliminó correctamente, False en caso contrario
        return self.task_repository.delete(task_id)
