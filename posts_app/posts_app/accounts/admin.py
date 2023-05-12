from django.contrib import admin

from posts_app.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
