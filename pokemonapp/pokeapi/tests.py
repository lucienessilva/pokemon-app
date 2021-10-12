from django.test import TestCase
from .models import Type, Pokemon


# Create your tests here.
class BaseTestCase(TestCase):
    def setUp(self):
        Type.objects.all().delete()
        Pokemon.objects.all().delete()
        """pokemon deleted not deletes related types"""
        self.t1 = Type.objects.create(name='Type1', id=1)
        self.t2 = Type.objects.create(name='Type2', id=2)
        self.t3 = Type.objects.create(name='Type3', id=3)

        self.p1 = Pokemon.objects.create(name='Pokemon1', id=1, weight=20, is_default=True)
        self.p2 = Pokemon.objects.create(name='Pokemon2', id=2, weight=20, is_default=True)
        self.p3 = Pokemon.objects.create(name='Pokemon3', id=3, weight=20, is_default=True)
        self.p1.types.add(self.t1)
        self.p1.types.add(self.t2)
        self.p1.save()
        self.p2.types.add(self.t3)
        self.p2.save()
        self.p3.types.add(self.t1)
        self.p3.save()


class PokemonTestCase(BaseTestCase):

    def test_pokemon_deletion_ok(self):
        self.p1.delete()
        self.p2.delete()
        self.assertEqual(Type.objects.count(), 3)
        self.assertEqual(Pokemon.objects.count(), 1)


class TypeTestCase(BaseTestCase):

    def test_type_deletion_ok(self):
        """type deleted deletes related pokemons"""

        self.t1.delete()
        self.assertEqual(Type.objects.count(), 2)
        self.assertEqual(Pokemon.objects.count(), 1)
        self.assertEqual(Pokemon.objects.all()[0].name, 'Pokemon2')
