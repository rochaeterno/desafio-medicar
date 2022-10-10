from asyncore import read
from rest_framework import serializers
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from medicar.models import Especialidade, Medico, Horario, Agenda, Consulta


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
        fields = ['id', 'crm', 'nome', 'email', 'created_at', 'updated_at']


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'horario']


class AgendaSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(read_only=True, many=True)
    medico = MedicoSerializer(many=False, read_only=True)

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia',
                  'horarios', 'created_at', 'updated_at']


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
