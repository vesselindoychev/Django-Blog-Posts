from django.urls import path

from posts_app.main.views import HomeView, PostListView, load_post_data_view, PostDetailsView, \
    like_unlike_post_view, create_post_view, CreatePostView, create_blog_post_view, load_blog_post_data_view, \
    BlogPostDetailsView

urlpatterns = (
    # Home
    path('', HomeView.as_view(), name='home'),

    # Posts with Normal Classed Based Views
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('post-details/<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('blog-post-details/<int:pk>/', BlogPostDetailsView.as_view(), name='blog-post-details'),

    # Posts with Function Based Views and AJAX requests
    path('posts/', create_post_view, name='posts list'),
    path('blog-posts/', create_blog_post_view, name='blog-posts-list'),

    path('data/<int:num_posts>/', load_post_data_view, name='post-data'),
    path('blog-data/<int:num_blog_posts>/', load_blog_post_data_view, name='blog-post-data'),

    path('like-unlike-post/', like_unlike_post_view, name='like-unlike-post'),
)