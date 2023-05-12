
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('posts_app.accounts.urls')),
    path('', include('posts_app.main.urls')),
]
