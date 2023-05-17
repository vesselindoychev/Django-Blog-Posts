from django.urls import path

from posts_app.main.views import HomeView, PostListView, load_post_data_view, PostDetailsView, \
    like_unlike_post_view, create_post_view, CreatePostView

urlpatterns = (
    # Home
    path('', HomeView.as_view(), name='home'),

    # Posts {

    # Class Based View
    path('create-post/', CreatePostView.as_view(), name='create-post'),

    # AJAX Function Based View
    path('posts/', create_post_view, name='posts list'),
    # path('posts/', PostListView.as_view(), name='posts list'),

    # {



    path('post-details/<int:pk>/', PostDetailsView.as_view(), name='post-details'),

    # Posts with AJAX
    path('data/<int:num_posts>/', load_post_data_view, name='post-data'),
    path('like-unlike-post/', like_unlike_post_view, name='like-unlike-post'),
    # path('create-post-ajax/', create_post_view, name='create-post-ajax'),
)