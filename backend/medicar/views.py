from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import date, datetime, timedelta
from medicar.models import Consulta
from medicar.serializer import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def list(self, request):
        query = Consulta.objects.filter(
            Q(agenda__dia__gt=date.today()) |
            Q(agenda__dia=date.today(), horario__horario__gt=datetime.now())
        ).order_by(
            'agenda__dia',
            'horario__horario'
        )
        serializer = ConsultaSerializer(query, many=True)
        return Response(serializer.data)
