from django.urls import path

from . import views

app_name = "bookmark"
urlpatterns = [
    path("", views.bookmark, name="bookmark"),
    path("import/", views.bookmark_upload, name="bookmark_import"),
]
