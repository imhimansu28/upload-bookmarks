import json

from django.core.management.base import BaseCommand

from teams.models import Category, Teams


def getJsonData(filname):
    file = open(filname, "r")
    x = file.read()
    jsonData = json.loads(x)
    return jsonData


def save_team_data(filename):
    jsonData = getJsonData(filename)
    teams = []
    for row in jsonData:
        teams.append(
            Teams(
                name=row["Team_Name"],
                code_name=row["Team_Short_Code"],
                category=Category.TEAMS_CATEGORY[3],
            )
        )
    Teams.objects.bulk_create(teams)
    return "data save successfully"


class Command(BaseCommand):
    help = "Fetch teams  from json file "

    def handle(self, *args, **options):
        filename = "tmp/data/team.json"
        save_team_data(filename)
