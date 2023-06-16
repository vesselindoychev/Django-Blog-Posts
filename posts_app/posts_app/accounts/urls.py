from django.urls import path

from posts_app.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileDetailsView, \
    EditProfileView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='edit-profile'),
)