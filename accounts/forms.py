from django import forms
from django.contrib.auth import get_user_model

from .models import UserProfile


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "username")

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "profile_image",
            "cover_image",
            "address",
            "github",
            "aboutus",
            "facebook",
            "instagram",
            "secondary_education",
            "higher_education",
        ]

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class EditProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)
    cover_image = forms.ImageField(required=False)

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "mobile_no",
            "date_of_birth",
        ]

    address = forms.CharField(required=False)
    secondary_education = forms.CharField(required=False)
    higher_education = forms.CharField(required=False)
    graduation = forms.BooleanField(required=False)
    aboutus = forms.CharField(required=False)
    specilization = forms.CharField(required=False)
    github = forms.URLField(required=False)
    linkedIn = forms.URLField(required=False)
    facebook = forms.URLField(required=False)
    instagram = forms.URLField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
        if self.instance:
            try:
                self.initial[
                    "profile_image"
                ] = self.instance.userprofile.profile_image
                self.initial[
                    "cover_image"
                ] = self.instance.userprofile.cover_image
                self.initial["address"] = self.instance.userprofile.address
                self.initial[
                    "secondary_education"
                ] = self.instance.userprofile.secondary_education
                self.initial[
                    "higher_education"
                ] = self.instance.userprofile.higher_education
                self.initial[
                    "graduation"
                ] = self.instance.userprofile.graduation
                self.initial["aboutus"] = self.instance.userprofile.aboutus
                self.initial[
                    "specilization"
                ] = self.instance.userprofile.specilization
                self.initial["github"] = self.instance.userprofile.github
                self.initial["linkedIn"] = self.instance.userprofile.linkedIn
                self.initial["facebook"] = self.instance.userprofile.facebook
                self.initial["instagram"] = self.instance.userprofile.instagram
            except UserProfile.DoesNotExist:
                pass

    def save(self, commit=True):
        user_base = super().save(commit=False)
        user_profile, created = UserProfile.objects.get_or_create(
            user=user_base
        )
        user_profile.profile_image = self.cleaned_data["profile_image"]
        user_profile.cover_image = self.cleaned_data["cover_image"]
        user_profile.address = self.cleaned_data["address"]
        user_profile.secondary_education = self.cleaned_data[
            "secondary_education"
        ]
        user_profile.higher_education = self.cleaned_data["higher_education"]
        user_profile.graduation = self.cleaned_data["graduation"]
        user_profile.aboutus = self.cleaned_data["aboutus"]
        user_profile.specilization = self.cleaned_data["specilization"]
        user_profile.github = self.cleaned_data["github"]
        user_profile.linkedIn = self.cleaned_data["linkedIn"]
        user_profile.facebook = self.cleaned_data["facebook"]
        user_profile.instagram = self.cleaned_data["instagram"]
        if commit:
            user_base.save()
            user_profile.save()
            created.save()
        return user_base
