from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from application.use_cases.task_use_cases import TaskUseCases
from infrastructure.django_app.repositories.task_repository import TaskRepositoryDjango
from infrastructure.django_app.serializers import TaskSerializerDRF


class TaskListCreateView(APIView):
    """
    Hereda de: APIView
    Propósito: Manejar endpoints para listar todas las tareas (GET) y crear nuevas (POST)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_cases = TaskUseCases(TaskRepositoryDjango())

    def get(self, request):
        # Método para obtener todas las tareas
        tasks = self.use_cases.get_all_tasks()
        serializer = TaskSerializerDRF(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Método para crear una nueva tarea
        serializer = TaskSerializerDRF(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            created_task = self.use_cases.create_task(
                title=data["title"], description=data["description"]
            )
            return Response(
                TaskSerializerDRF(created_task).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveUpdateDeleteView(APIView):
    """
    Hereda de: APIView
    Propósito: Manejar operaciones sobre tareas individuales
    - GET: Obtener una tarea específica
    - PUT: Actualizar una tarea
    - DELETE: Eliminar una tarea
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_cases = TaskUseCases(TaskRepositoryDjango())

    def get(self, request, pk):
        # Obtener una tarea por ID
        task = self.use_cases.get_task_by_id(pk)
        if not task:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(TaskSerializerDRF(task).data)

    def put(self, request, pk):
        # Actualizar una tarea existente
        serializer = TaskSerializerDRF(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            updated_task = self.use_cases.update_task(
                task_id=pk,
                title=data["title"],
                description=data["description"],
                completed=data["completed"],
            )
            if updated_task:
                return Response(TaskSerializerDRF(updated_task).data)
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        # Obtener la tarea existente
        task = self.use_cases.get_task_by_id(pk)
        if not task:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        # Validar los datos parciales
        serializer = TaskSerializerDRF(data=request.data, partial=True)
        if serializer.is_valid():
            # Actualizar solo los campos proporcionados
            data = serializer.validated_data
            updated_task = self.use_cases.update_task(
                task_id=pk,
                title=data.get("title", task.title),
                description=data.get("description", task.description),
                completed=data.get("completed", task.completed),
            )
            return Response(TaskSerializerDRF(updated_task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Eliminar una tarea
        deleted = self.use_cases.delete_task(pk)
        if deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
