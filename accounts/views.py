from django.shortcuts import render


# Create your views here.
def create_user(request):
    return render(request, "register.html")


def signin(request):
    return render(request, "login.html")


def edit_profile(request):
    return render(request, "edit-profile.html")


def view_profile(request):
    return render(request, "view-profile.html")


def forget_password(request):
    return render(request, "forget-password.html")


def change_password(request):
    return render(request, "change-password.html")
