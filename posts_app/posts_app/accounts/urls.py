from django.urls import path

from posts_app.accounts.views import LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
)