from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .services import TaskServices

class TaskAPIView(APIView):
    def __init__(self, **kwargs):
        self.servicos = TaskServices() 
        super().__init__(**kwargs)

    def get(self, request, pk=None):
        if pk:
            task = self.servicos.filtrarPorId(pk)
            if task:
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        titulo = request.query_params.get('titulo')

        tarefas = self.servicos.filtrarPorDatas(data_inicio, data_fim)
        if titulo:
            tarefas = self.servicos.filtrarPorTitulo(titulo)

        serializer = TaskSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        task = self.servicos.filtrarPorId(pk)
        if not task:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            task_atualizada = self.servicos.atualizarTarefa(task, serializer.validated_data)
            return Response(TaskSerializer(task_atualizada).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.servicos.filtrarPorId(pk)
        if not task:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
