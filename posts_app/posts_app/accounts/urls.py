from django.urls import path

from posts_app.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileDetailsView, \
    EditProfileView, load_countries_and_cities

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile-details'),
    path('edit/<int:pk>/', EditProfileView.as_view(), name='edit-profile'),

    path('ajax/load-cities/', load_countries_and_cities, name='ajax-load-cities'),
)