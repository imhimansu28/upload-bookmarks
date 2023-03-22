from django.contrib import admin

from .models import UserBase, UserProfile

admin.site.register(UserBase)
admin.site.register(UserProfile)
