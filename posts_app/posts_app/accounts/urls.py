from django.urls import path

from posts_app.accounts.views import LoginUserView, RegisterUserView, LogoutUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
)