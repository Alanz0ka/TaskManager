from django.utils.dateparse import parse_date
from .models import Task
from datetime import date

class TaskServices:
    def filtrarPorDatas(self, data_inicio=None, data_fim=None):
        if data_inicio and data_fim:
            try:
                data_inicio = parse_date(data_inicio)
                data_fim = parse_date(data_fim)
                if data_inicio and data_fim:
                    return Task.objects.filter(data__range=[data_inicio, data_fim])
                else:
                    raise ValueError('Formato de data inválido. Use YYYY-MM-DD')
            except ValueError:
                raise ValueError('Formato de data inválido. Use YYYY-MM-DD')

        elif data_inicio:
            try:
                data_inicio = parse_date(data_inicio)
                if data_inicio:
                    return Task.objects.filter(data=data_inicio)
                else:
                    raise ValueError('Formato de data inválido. Use YYYY-MM-DD')
            except ValueError:
                raise ValueError('Formato de data inválido. Use YYYY-MM-DD')
            
        else:
            return Task.objects.all()

    def filtrarPorTitulo(self, consulta):
        return Task.objects.filter(titulo__icontains=consulta)

    def filtrarPorId(self, id):
        try:
            return Task.objects.get(pk=id)
        except Task.DoesNotExist:
            return None

    def atualizarTarefa(self, task, dados_validados):
        task.titulo = dados_validados.get('titulo', task.titulo)
        task.descricao = dados_validados.get('descricao', task.descricao)
        task.data = dados_validados.get('data', task.data)
        task.horario = dados_validados.get('horario', task.horario)
        task.save()
        return task
