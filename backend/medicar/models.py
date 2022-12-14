from email.policy import default
from enum import unique
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date, datetime


class Especialidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.ForeignKey(
        to=Especialidade,
        on_delete=models.SET_NULL,
        related_name="medicos",
        null=True,
        blank=False
    )
    crm = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        unique=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9999)
        ]
    )
    email = models.EmailField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Horario(models.Model):
    horario = models.TimeField(
        auto_now=False, auto_now_add=False, unique=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.horario)


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
    horarios = models.ManyToManyField(Horario, through='AgendaHorario',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        medico_conflitante = Agenda.objects.filter(
            dia=self.dia, medico_id=self.medico.id).last()

        if self.id is None and self.dia < date.today():
            raise ValidationError(
                "N??o ?? possivel cadastrar uma agenda retroativamente.")

        if self.id is None and medico_conflitante is not None:
            raise ValidationError(
                "O medico selecionado j?? possui uma agenda cadastrada para o dia selecionado.")


class AgendaHorario(models.Model):
    agenda = models.ForeignKey(
        Agenda, on_delete=models.CASCADE, related_name='through_model')
    horario = models.ForeignKey(
        Horario, on_delete=models.CASCADE, related_name='through_model')
    _esta_ocupado = models.BooleanField(default=False)

    def clean(self):
        trought_table = self

        if self.id is None and trought_table.agenda.dia == date.today() and trought_table.horario.horario < datetime.now().time():
            raise ValidationError(
                "N??o ?? possivel horario passado em uma agenda.")


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
