from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fileds):

        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fileds):
        extra_fileds.setdefault("is_staff", True)
        extra_fileds.setdefault("is_superuser", True)
        extra_fileds.setdefault("is_active", True)

        if extra_fileds.get("is_staff") is not True:
            raise ValueError(("Superuser is must have a staff true"))
        return self.create_user(email, password, **extra_fileds)


class UserBase(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15)
    date_of_birth = models.DateField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "mobile_no",
        "date_of_birth",
    ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=("profile"),
        on_delete=models.CASCADE,
    )
    profile_image = models.FileField(
        upload_to="media/user/profie/",
        blank=True,
    )
    cover_image = models.FileField(
        upload_to="media/user/cover/",
        blank=True,
    )
    address = models.TextField(default="")
    secondary_education = models.CharField(max_length=150, blank=True)
    higher_education = models.CharField(max_length=150, blank=True)
    graduation = models.BooleanField(
        default=False,
    )
    aboutus = models.TextField(default="")
    specilization = models.CharField(default="", max_length=150)
    github = models.URLField(blank=True)
    linkedIn = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
