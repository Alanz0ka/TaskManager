from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .services import TaskServices
from .google_calendar import iniciar_google_calendar, criar_evento

class TaskAPIView(APIView):
    def __init__(self, **kwargs):
        self.servicos = TaskServices() 
        self.calendar_service = iniciar_google_calendar()
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
            task = serializer.save()  # Salva a tarefa e obtém a instância da tarefa

            data_inicio = f"{task.data}T{task.horario if task.horario else '00:00:00'}"
            data_fim = f"{task.data}T{task.horario if task.horario else '23:59:59'}"
            criar_evento(
                self.calendar_service,
                resumo=task.titulo,
                descricao=task.descricao,
                data_inicio=data_inicio,
                data_fim=data_fim
            )
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
        
        self.servicos.deletarTarefa(task)  # Use o serviço para deletar a tarefa
        return Response(status=status.HTTP_204_NO_CONTENT)
