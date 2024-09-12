# Generated by Django 5.1.1 on 2024-09-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, default='', null=True)),
                ('data', models.DateField()),
                ('horario', models.TimeField(null=True)),
            ],
        ),
    ]
