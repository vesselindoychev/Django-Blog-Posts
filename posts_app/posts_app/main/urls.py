from django.urls import path

from posts_app.main.views import HomeView, CreatePostView, PostListView, load_post_data_view, PostDetailsView

urlpatterns = (
    # Home
    path('', HomeView.as_view(), name='home'),

    # Posts
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('posts/', PostListView.as_view(), name='posts list'),
    path('post-details/<int:pk>/', PostDetailsView.as_view(), name='post-details'),

    # Posts with AJAX
    path('data/<int:num_posts>/', load_post_data_view, name='post-data'),
)