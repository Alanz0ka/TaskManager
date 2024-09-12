from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data', 'horario')

admin.site.register(Task, TaskAdmin)