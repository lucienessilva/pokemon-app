from django.core.management.base import BaseCommand
from pokeapi.models import Type, Pokemon
import logging
import requests
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.db import transaction

""" Clear all data and get first 20 pokemons """
MODE_REFRESH = 'refresh'

""" Clear all data"""
MODE_CLEAR = 'clear'

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = "seed database with pokemons and types."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding pokemons...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete all types and pokemons instances")
    Type.objects.all().delete()
    Pokemon.objects.all().delete()


def get_pokeapi_data(url):
    """get data from poke api endpoint"""
    logger.info("getting poke api data {}".format(url))
    val = URLValidator()
    try:
        val(url)
    except ValidationError as err:
        logger.error("Invalid url: {}", url)
        logger.error(err)
        return False

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as errh:
        logger.info("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        logger.info("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        logger.info("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        logger.info("OOps: Something Else", err)
    return False


def run_seed(self, mode):
    """ Seed database based on mode
    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # get the pokemon list
    pokemons_list = get_pokeapi_data('https://pokeapi.co/api/v2/pokemon/')

    # verifies if list has pokemons
    if pokemons_list and "results" in pokemons_list and len(pokemons_list["results"]) > 0:
        logger.info("{} pokemons listed".format(len(pokemons_list['results'])))
    else:
        # if no pokemons, just log and return
        logger.error("no pokemons listed")
        return

    # for each item in pokemon list get its data
    for poke_item in pokemons_list['results']:
        poke_data = get_pokeapi_data(poke_item['url'])
        if poke_data:
            # to avoid inconsistency, we will save pokemon and its types within the same transaction
            with transaction.atomic():
                # create pokemon object
                pokemon_obj = Pokemon(is_default=bool(poke_data['is_default']), id=poke_data['id'], name=poke_data['name'], weight=poke_data["weight"])
                pokemon_obj.save()
                # for each type in pokemon json data, get its own data
                for type_item in poke_data['types']:
                    type_data = get_pokeapi_data(type_item["type"]["url"])
                    if type_data:
                        # if type data returned, verifies if it already exists or needs to be created
                        type_count = Type.objects.filter(id = type_data['id']).count()
                        if type_count == 0:
                            type_obj = Type(id=type_data["id"], name=type_data["name"])
                            type_obj.save()
                        pokemon_obj.types.add(type_obj)
                        pokemon_obj.save()
                    else:
                        logger.error("no data for type {}".format(type_item['name']))

        else:
            logger.error("no data for pokemon {}".format(poke_item['name']))
