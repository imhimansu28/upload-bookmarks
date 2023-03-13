from django.shortcuts import render


def bookmark(request):
    return render(request, "bookmark.html")
