from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from clientes.models import Cliente
from clientes.serializers import ClienteSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome']
    serializer_class = ClienteSerializer
