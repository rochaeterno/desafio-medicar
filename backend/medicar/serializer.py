from rest_framework import serializers
from medicar.models import Especialidade, Medico, Horario, Agenda, Consulta


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

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia',
                  'horarios', 'created_at', 'updated_at']


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'agenda', 'horario',
                  'paciente', 'created_at', 'updated_at']
