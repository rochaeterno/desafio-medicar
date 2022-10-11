from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response
from datetime import date, datetime
from medicar.models import Consulta, Agenda
from medicar.serializer import ConsultaSerializer, AgendaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from medicar.filtersets import AgendaFilter


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def list(self, request):
        query = Consulta.objects.filter(
            Q(agenda__dia__gt=date.today()) |
            Q(
                agenda__dia=date.today(),
                horario__horario__gt=datetime.now()
            )
        ).order_by(
            'agenda__dia',
            'horario__horario'
        )
        serializer = ConsultaSerializer(query, many=True)
        return Response(serializer.data)


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

    def list(self, request):
        query = Agenda.objects.filter(
            dia__gte=date.today(), _esta_lotada=False
        ).order_by('dia')
        self.filter_queryset(query)
        serializer = AgendaSerializer(query, many=True)
        return Response(serializer.data)


class AgendaFilter(generics.ListAPIView):
    queryset = Agenda.objects.filter(
        dia__gte=date.today(), _esta_lotada=False
    ).order_by('dia')
    serializer_class = AgendaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AgendaFilter
