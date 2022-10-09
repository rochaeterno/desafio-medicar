import email
from django.db import models
from django.contrib.auth.models import User


class Especialidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Medico(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.ForeignKey(
        to=Especialidade,
        on_delete=models.SET_NULL,
        related_name="medicos",
        null=True,
        blank=False
    )
    email = models.EmailField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Horario(models.Model):
    horario = models.TimeField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Agenda(models.Model):
    medico = models.ForeignKey(
        to=Medico,
        on_delete=models.CASCADE,
        related_name="agendas",
        null=False,
        blank=False
    )
    dia = models.DateField(
        null=False,
        blank=False
    )
    horarios = models.ManyToManyField(Horario)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Consulta(models.Model):
    agenda = models.ForeignKey(
        to=Agenda,
        on_delete=models.CASCADE,
        related_name="consultas",
        null=False,
        blank=False
    )
    horario = models.ForeignKey(
        to=Horario,
        on_delete=models.CASCADE,
        related_name="consultas",
        null=False,
        blank=False
    )
    paciente = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="consultas",
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
