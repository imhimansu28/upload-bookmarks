import json

from django.core.management.base import BaseCommand

from bookmark.models import Bookmark


def getJsonData(filname):
    file = open(filname, "r")
    x = file.read()
    jsonData = json.loads(x)
    return jsonData


def save_bookmark_data(filename):
    jsonData = getJsonData(filename)
    bookmark = []
    for row in jsonData:
        bookmark.append(Bookmark(title=row["title"], url=row["url"]))
    Bookmark.objects.bulk_create(bookmark)
    return "data save successfully"


class Command(BaseCommand):
    help = "Fetch bookmark  from json file "

    def handle(self, *args, **options):
        filename = "temp/data/chrome_bookmarks.json"
        save_bookmark_data(filename)
