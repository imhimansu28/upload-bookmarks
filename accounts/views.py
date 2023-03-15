from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AccountCreationForm, LoginForm
from .models import UserBase


# Create your views here.
def create_user(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect("accounts:login")

    else:
        form = AccountCreationForm()
    return render(request, "register.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # validate email and password
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("accounts:view_profile")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "login.html", context)


@login_required
def edit_profile(request):
    return render(request, "edit-profile.html")


@login_required
def view_profile(request):
    user = UserBase.objects.get(id=request.user.id)
    return render(request, "view-profile.html", {"user": user})


def forget_password(request):
    return render(request, "forget-password.html")


@login_required
def change_password(request):
    return render(request, "change-password.html")


@login_required
def logout_request(request):
    logout(request)
    return redirect("accounts:login")
