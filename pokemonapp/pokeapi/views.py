from rest_framework import viewsets, permissions
from .models import Pokemon, Type
from .serializers import PokemonSerializer, TypeSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pokemons to be viewed or edited.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = [permissions.AllowAny]


class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows types to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.AllowAny]
