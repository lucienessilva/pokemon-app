from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'types', views.TypeViewSet)
router.get_api_root_view().cls.__name__ = "PokeApi"
router.get_api_root_view().cls.__doc__ = "Integração Django PokeApi"

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]