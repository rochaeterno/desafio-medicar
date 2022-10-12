import django_filters
from medicar.models import Agenda, Medico


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
    data_inicio = django_filters.DateFilter(
        field_name='dia', lookup_expr='gte')
    data_final = django_filters.DateFilter(field_name='dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = ['medico', 'dia']
