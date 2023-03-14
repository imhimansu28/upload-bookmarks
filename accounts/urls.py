from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.signin, name="login"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("view-profile/", views.view_profile, name="view_profile"),
    path("forget-password/", views.forget_password, name="forget_password"),
    path("change-password/", views.change_password, name="change_password"),
]
