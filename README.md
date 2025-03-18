# Backend API con Django REST Framework

API REST para gestión de tareas implementando Clean Architecture.

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

## Endpoints

- `GET /api/tasks/`: Listar tareas
- `POST /api/tasks/`: Crear tarea
- `GET /api/tasks/{id}/`: Ver tarea
- `PUT /api/tasks/{id}/`: Actualizar tarea
- `PATCH /api/tasks/{id}/`: Actualización parcial
- `DELETE /api/tasks/{id}/`: Eliminar tarea
