from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import AccountCreationForm, EditProfileForm
from .models import UserBase, UserProfile


def create_user(request):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.create(user=user)
            profile.save()
            login(request, user)
            return redirect(
                "accounts:view_profile"
            )  # change "accounts:login" to your home page URL

    else:
        form = AccountCreationForm()
    return render(request, "register.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request=request, username=username, password=password
            )
            if user is not None:
                login(request, user)
                return redirect("accounts:view_profile")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)


@login_required
def edit_profile(request):
    user_base = request.user
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=user_base)
        if form.is_valid():

            form.save()
            return redirect("accounts:view_profile")
    else:
        form = EditProfileForm(instance=user_base)

    context = {
        "form": form,
    }
    return render(request, "edit-profile.html", context)


@login_required
def view_profile(request):
    user = UserBase.objects.get(id=request.user.id)
    return render(request, "view-profile.html", {"user": user})


def forget_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            user = UserBase.objects.get(email=user_email)
            current_site = settings.SITE_URL
            mail_subject = "Reset your password on {}".format(current_site)
            message = render_to_string(
                "reset_password_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["imhimansu28@gmail.com"],
            )
            messages.success(
                request,
                "We have sent an email to reset your password.\
                      Please check your inbox.",
            )
            return redirect("accounts:login")
    else:
        form = PasswordResetForm()
    return render(request, "forget-password.html", {"form": form})


@login_required
def change_password(request):
    return render(request, "change-password.html")


@login_required
def logout_request(request):
    logout(request)
    return redirect("accounts:login")
