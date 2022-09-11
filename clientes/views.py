from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # Colocando em ordem a lista de clientes
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']

    # Filtrando dados da API (filters.SearchFilter)
    # filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'cpf', 'rg','ativo']
    
    # Mostra os clientes ATIVOS e INATIVOS
    filterset_fields = ["ativo"]