from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from datetime import date, datetime
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from medicar.models import Especialidade, Medico, Horario, Agenda, Consulta, AgendaHorario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome']


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'email']


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'horario']


class AgendaHorarioSerializer(serializers.ModelSerializer):
    horario = serializers.SerializerMethodField()

    class Meta:
        model = AgendaHorario
        fields = ['horario', '_esta_ocupado']

    def get_horario(self, obj):
        return (obj.horario.horario)


class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.SerializerMethodField()
    medico = MedicoSerializer(many=False, read_only=True)
    dia = serializers.SerializerMethodField()

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia',
                  'horarios', 'created_at', 'updated_at']

    def get_dia(self, obj):
        return (obj.dia.strftime('%d/%m/%Y'))

    def get_horarios(self, obj):
        horarios_validos = []
        horarios_preenchidos = []

        for instance in obj.agendahorario_set.all():
            valide = instance.horario.horario >= datetime.now().time(
            ) and instance.agenda.dia == date.today() and not instance._esta_ocupado
            if valide or instance.agenda.dia > date.today() and not instance._esta_ocupado:
                horarios_validos.append(instance.horario.horario)
        return (set(horarios_validos) - set(horarios_preenchidos))


class ConsultaSerializer(serializers.ModelSerializer):
    medico = serializers.SerializerMethodField()
    dia = serializers.SerializerMethodField()
    horario = serializers.SerializerMethodField()
    data_agendamento = serializers.DateTimeField(source='created_at')

    class Meta:
        model = Consulta
        fields = [
            'id',
            'dia',
            'horario',
            'data_agendamento',
            'medico'
        ]

    def get_medico(self, obj):
        return (model_to_dict(obj.agenda.medico))

    def get_dia(self, obj):
        return (obj.agenda.dia.strftime('%d/%m/%Y'))

    def get_horario(self, obj):
        return (obj.horario.horario)


class ConsultaStoreSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()

    def save(self):
        agenda_id = self.validated_data['agenda_id']
        horario = self.validated_data['horario']

        agenda = Agenda.objects.get(pk=agenda_id)
        horario = Horario.objects.get(horario=horario)
        paciente = User.objects.get(pk=1)

        consulta = Consulta(agenda=agenda, horario=horario, paciente=paciente)
        AgendaHorario.objects.filter(
            agenda_id=agenda_id, horario_id=horario.id).update(_esta_ocupado=True)
        consulta.save()
        return ConsultaSerializer(consulta).data
