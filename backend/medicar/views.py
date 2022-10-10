from rest_framework import viewsets

from medicar.models import Consulta
from medicar.serializer import ConsultaSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer