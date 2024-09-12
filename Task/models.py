from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=150, null=False)
    descricao = models.TextField(null=True, blank=True, default='')
    data = models.DateField(null=False)
    horario = models.TimeField(null=True)

    def __str__(self):
        return self.titulo
    