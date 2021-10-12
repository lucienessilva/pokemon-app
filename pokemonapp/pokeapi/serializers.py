from rest_framework import serializers
from .models import Type, Pokemon


class TypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Type
        fields = ['id', 'name', 'hexadecimal_color']


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    types = serializers.HyperlinkedRelatedField(many=True, view_name='type-detail', read_only=True)

    class Meta:
        model = Pokemon
        fields = ['url', 'id', 'name', 'is_default', 'weight', 'types']
