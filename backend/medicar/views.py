from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.response import Response
from datetime import date, datetime
from medicar.models import Consulta, Agenda, AgendaHorario
from medicar.serializer import ConsultaSerializer, AgendaSerializer, ConsultaStoreSerializer, ConsultaDestroySerializer
from django_filters.rest_framework import DjangoFilterBackend
from medicar.filtersets import AgendaFilter


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def create(self, request, *args, **kwargs):
        serializer = ConsultaStoreSerializer(
            data=request.data, context={"req": request})
        data = {}
        if serializer.is_valid():
            consulta = serializer.save()
            data = consulta
        else:
            data = serializer.errors

        return Response(data)

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

    def destroy(self, request, *args, **kwargs):
        data = {}
        response = {}
        data['id'] = self.kwargs['pk']
        serializer = ConsultaDestroySerializer(
            data=data, context={"req": request, 'pk': self.kwargs['pk']})

        if (serializer.is_valid()):
            consulta = Consulta.objects.get(pk=self.kwargs['pk'])
            AgendaHorario.objects.filter(
                agenda_id=consulta.agenda.id,
                horario_id=consulta.horario.id
            ).update(_esta_ocupado=False)
            consulta.delete()
        else:
            response = serializer.errors

        return Response(response)


class AgendaListAPIView(generics.ListAPIView):
    queryset = Agenda.objects.filter(
        dia__gte=date.today(), _esta_lotada=False
    ).order_by('dia')
    serializer_class = AgendaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AgendaFilter
