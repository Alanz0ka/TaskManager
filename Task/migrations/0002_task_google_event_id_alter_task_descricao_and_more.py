# Generated by Django 5.1.1 on 2024-09-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='google_event_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='horario',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
