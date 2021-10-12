from django.contrib import admin
from .models import *
from django.db import transaction


class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display = ['name', 'hexadecimal_color']
    ordering = ['name']

    # override the default delete_queryset to remove all the pokemons associated
    def delete_queryset(self, request, queryset):
        with transaction.atomic():
            for obj in queryset:
                Pokemon.objects.filter(types__pk=obj.id).delete()
                obj.delete()

    # override the default delete_model to remove all the pokemons associated
    def delete_model(self, request, obj):
        with transaction.atomic():
            Pokemon.objects.filter(types__pk=obj.id).delete()
            obj.delete()


# Register your models here.
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight', 'is_default']
    ordering = ['name']


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)
