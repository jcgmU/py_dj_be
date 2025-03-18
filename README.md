# Backend API con Django REST Framework

API REST para gestión de tareas implementando Clean Architecture.

## Arquitectura

Este proyecto implementa Clean Architecture con las siguientes capas:

```
Backend/
├── domain/             # Reglas de negocio y entidades
├── application/        # Casos de uso
├── infrastructure/     # Frameworks y adaptadores
└── interface_adapters/ # Interfaces y presentadores
```

### Flujo de la Aplicación

1. La petición HTTP llega a las vistas (Views)
2. Las vistas utilizan casos de uso (Use Cases)
3. Los casos de uso implementan la lógica de negocio
4. Los repositorios manejan la persistencia de datos
5. Las entidades representan los objetos del dominio

## Requisitos

- Python 3.8+
- Django 4.2+
- Django REST Framework

## Instalación

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate
```

## Uso

```bash
python manage.py runserver
```

La API estará disponible en: http://localhost:8000/api/tasks/

## Endpoints y Flujo de Datos

### GET /api/tasks/

- **Propósito**: Listar todas las tareas
- **Flujo**:
  1. View recibe la petición
  2. UseCase.get_all_tasks() es invocado
  3. Repository.find_all() obtiene datos
  4. Serializer convierte TaskEntity a JSON
- **Respuesta**: Lista de tareas ordenadas por fecha

### POST /api/tasks/

- **Propósito**: Crear nueva tarea
- **Payload**:

```json
{
  "title": "string",
  "description": "string",
  "completed": false
}
```

- **Flujo**:
  1. Serializer valida datos
  2. UseCase.create_task() procesa
  3. Repository.save() persiste
  4. Retorna tarea creada

### GET /api/tasks/{id}/

- **Propósito**: Obtener tarea específica
- **Flujo**:
  1. View valida ID
  2. UseCase.get_task_by_id() busca
  3. Repository.find_by_id() recupera
  4. Serializer prepara respuesta

### PUT /api/tasks/{id}/

- **Propósito**: Actualizar tarea completa
- **Payload**: Todos los campos requeridos
- **Flujo**:
  1. Serializer valida datos completos
  2. UseCase.update_task() procesa
  3. Repository.save() actualiza
  4. Retorna tarea modificada

### PATCH /api/tasks/{id}/

- **Propósito**: Actualización parcial
- **Payload**: Solo campos a modificar
- **Flujo**:
  1. Serializer valida datos parciales
  2. UseCase.update_task() actualiza
  3. Repository mantiene campos no modificados
  4. Retorna tarea actualizada

### DELETE /api/tasks/{id}/

- **Propósito**: Eliminar tarea
- **Flujo**:
  1. View valida ID
  2. UseCase.delete_task() procesa
  3. Repository.delete() elimina
  4. Retorna 204 No Content

## Estructura de Datos

### TaskEntity

```python
class TaskEntity:
    id: Optional[int]
    title: str
    description: str
    completed: bool
    created_at: Optional[datetime]
```

## Manejo de Errores

- 400: Bad Request (datos inválidos)
- 404: Not Found (tarea no existe)
- 500: Internal Server Error

## Pruebas

```bash
python manage.py test
```
