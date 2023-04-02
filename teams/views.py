from django.shortcuts import render

from .models import Category, Teams

# Create your views here.


def view_team(request):
    category = request.get["category"]
    teams = Teams.objects.filter(category=category)
    return render(request, "team.html", {"teams": teams})
