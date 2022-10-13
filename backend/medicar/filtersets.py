import django_filters
from medicar.models import Agenda, Medico, Especialidade


class AgendaFilter(django_filters.FilterSet):
    medico = django_filters.ModelMultipleChoiceFilter(
        field_name='medico__id',
        to_field_name='id',
        queryset=Medico.objects.all()
    )
    crm = django_filters.ModelMultipleChoiceFilter(
        field_name='medico__crm',
        to_field_name='crm',
        queryset=Medico.objects.all()
    )
    especialidade = django_filters.ModelMultipleChoiceFilter(
        field_name='medico__especialidade_id',
        to_field_name='especialidade_id',
        queryset=Medico.objects.all()
    )
    data_inicio = django_filters.DateFilter(
        field_name='dia', lookup_expr='gte')
    data_final = django_filters.DateFilter(field_name='dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = ['medico', 'dia']


class MedicoFilter(django_filters.FilterSet):
    especialidade = django_filters.ModelMultipleChoiceFilter(
        field_name='id',
        to_field_name='id',
        queryset=Especialidade.objects.all()
    )

    class Meta:
        model = Medico
        fields = ['especialidade']
