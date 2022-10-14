from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
import json
from datetime import date, datetime
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from medicar.models import Especialidade, Medico, Horario, Agenda, Consulta, AgendaHorario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        def validate_email(data):
            try:
                User.objects.get(email=data['email'])
                raise serializers.ValidationError(
                    {'email': 'Um usuário com este email já existe.'})
            except User.DoesNotExist:
                pass

        validate_email(data)
        return data

    def save(self,):
        user = User(
            username=self.validated_data['email'], email=self.validated_data['email'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ['id', 'nome']


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = serializers.SerializerMethodField()

    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'email', 'especialidade']

    def get_especialidade(self, obj):
        return (model_to_dict(obj.especialidade))


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


class FilterAgendaListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        agendas = data.filter(dia__gte=date.today())
        for agenda in agendas:
            horarios_livres = 0
            for horario in agenda.agendahorario_set.all():
                if horario._esta_ocupado == False:
                    if agenda.dia > date.today() or horario.horario.horario >= datetime.now().time() and agenda.dia == date.today():
                        horarios_livres += 1
            if horarios_livres == 0 or agenda.horarios.count() < 1:
                agendas = agendas.exclude(dia=agenda.dia)

        return super(FilterAgendaListSerializer, self).to_representation(agendas)


class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.SerializerMethodField()
    medico = MedicoSerializer(many=False, read_only=True)
    dia = serializers.SerializerMethodField()

    class Meta:
        model = Agenda
        list_serializer_class = FilterAgendaListSerializer
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
    medico = MedicoSerializer(source='agenda.medico')
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

    # def get_medico(self, obj):
    #     return model_to_dict(obj.agenda.medico)

    def get_dia(self, obj):
        return (obj.agenda.dia.strftime('%d/%m/%Y'))

    def get_horario(self, obj):
        return (obj.horario.horario)


class ConsultaStoreSerializer(serializers.Serializer):
    agenda_id = serializers.IntegerField()
    horario = serializers.TimeField()

    def validate(self, data):
        agenda_id = data['agenda_id']
        horario = data['horario']

        horario_instance = {}
        agenda = {}

        # Responsavel por testar a existencia da agenda selecionada
        try:
            agenda = Agenda.objects.get(pk=agenda_id)
        except ObjectDoesNotExist:
            raise ValidationError(
                {'message': 'A agenda selecionada não existe em nosso banco de dados.'})

         # Responsavel por testar a existencia do horário selecionado
        try:
            horario_instance = Horario.objects.get(horario=horario)
        except ObjectDoesNotExist:
            raise ValidationError(
                {'message': 'O horário selecionado não existe.'})

        """
        Responsavel por testar se a agenda selecionada esta
        relacionada com o horario selecionado e se este por sua vez
        está livre.
        """
        try:
            AgendaHorario.objects.get(
                agenda_id=agenda_id, horario_id=horario_instance.id, _esta_ocupado=False
            )
        except ObjectDoesNotExist:
            raise ValidationError(
                {'message': 'O horário selecionado não existe nesta agenda ou já está ocupado.'})

        """
        Responsavel por testar se a agenda selecionada é de um dia futuro
        e caso seja para hoje se o horario selecionado já passou.
        """
        if agenda.dia < date.today() or agenda.dia == date.today() and horario <= datetime.now().time():
            raise serializers.ValidationError(
                {'message': 'Não é possivel cadastrar uma consulta em uma data ou hora passadas.'})
        return data

    def save(self):
        agenda_id = self.validated_data['agenda_id']
        horario = self.validated_data['horario']

        agenda = Agenda.objects.get(pk=agenda_id)
        horario_instance = Horario.objects.get(horario=horario)
        paciente = User.objects.get(pk=1)

        consulta = Consulta(
            agenda=agenda, horario=horario_instance, paciente=paciente)
        AgendaHorario.objects.filter(
            agenda_id=agenda_id, horario_id=horario_instance.id).update(_esta_ocupado=True)
        consulta.save()

        return ConsultaSerializer(consulta).data


class ConsultaDestroySerializer(serializers.Serializer):
    def validate(self, data):
        consulta = {}
        try:
            consulta = Consulta.objects.get(id=self.context['pk'])
        except ObjectDoesNotExist:
            raise ValidationError(
                {'message': 'Esta consulta não existe em nosso banco de dados.'})

        if consulta.agenda.dia < date.today() or consulta.agenda.dia == date.today() and consulta.horario <= datetime.now().time():
            raise serializers.ValidationError(
                {'message': 'Não é possivel desmarcar uma consulta que já aconteceu.'})
        return data
