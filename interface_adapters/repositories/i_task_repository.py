# Importamos las herramientas necesarias:
# ABC y abstractmethod son para crear clases abstractas (interfaces)
from abc import ABC, abstractmethod

# List y Optional son tipos de datos especiales de Python
from typing import List, Optional

# Importamos la entidad TaskEntity que representa una tarea
from domain.entities.task_entity import TaskEntity


# Definimos una interfaz (clase abstracta) llamada ITaskRepository
# ABC significa "Abstract Base Class" - Es como un contrato que otras clases deben seguir
class ITaskRepository(ABC):

    # @abstractmethod indica que este método DEBE ser implementado por las clases hijas
    # find_all() devuelve una lista de todas las tareas
    # -> List[TaskEntity] indica que retorna una lista de objetos TaskEntity
    @abstractmethod
    def find_all(self) -> List[TaskEntity]:
        pass

    # find_by_id busca una tarea específica por su ID
    # Optional significa que puede devolver un TaskEntity o None si no se encuentra
    @abstractmethod
    def find_by_id(self, task_id: int) -> Optional[TaskEntity]:
        pass

    # save guarda una nueva tarea o actualiza una existente
    # Recibe un TaskEntity y devuelve el mismo objeto actualizado
    @abstractmethod
    def save(self, task: TaskEntity) -> TaskEntity:
        pass

    # delete elimina una tarea por su ID
    # Retorna True si se eliminó correctamente, False si no
    @abstractmethod
    def delete(self, task_id: int) -> bool:
        pass
