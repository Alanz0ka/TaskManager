from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True) 
    data = models.DateField()
    horario = models.TimeField(blank=True, null=True)
    google_event_id = models.CharField(max_length=255, blank=True, null=True, default='')

    def __str__(self):
        return self.titulo
