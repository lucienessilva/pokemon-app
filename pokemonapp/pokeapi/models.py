from django.db import models
from django.db import transaction


# Create your models here.
class Type(models.Model):
    class Meta:
        db_table = 'type'
        ordering = ['name']

    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    hexadecimal_color = models.CharField(max_length=7, null=True, blank=False)

    def __str__(self):
        return self.name

    # override delete method to delete pokemons related too
    def delete(self, *args, **kwargs):
        with transaction.atomic():
            Pokemon.objects.filter(types__pk=self.id).delete()
            super().delete(*args, **kwargs)


class Pokemon(models.Model):
    class Meta:
        db_table = 'pokemon'
        ordering = ['name']

    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    weight = models.IntegerField(null=False)
    is_default = models.BooleanField(null=False)
    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.name
