from django.contrib import admin

from posts_app.main.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
