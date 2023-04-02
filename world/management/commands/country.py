import json

from django.core.management.base import BaseCommand

from world.models import Country


def getJsonData(filename):
    file = open(filename, "r")
    x = file.read()
    jsonData = json.loads(x)
    return jsonData


def save_country(filename):
    jsonData = getJsonData(filename)
    world = []
    for row in jsonData:
        world.append(Country(name=row["name"], code=row["code"]))
        print("Country = ", row["name"], row["code"])
    Country.objects.bulk_create(world)
    total = len(world)
    return total


class Command(BaseCommand):
    help = "Fetch world  from json file "

    def handle(self, *args, **options):
        filename = "tmp/data/country.json"
        country = save_country(filename)
        print(f"Total country saved: %s" % country)
