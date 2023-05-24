from django.urls import path

from posts_app.main.views import HomeView, PostListView, load_post_data_view, PostDetailsView, \
    like_unlike_post_view, create_post_view, CreatePostView, create_blog_post_view, load_blog_post_data_view, \
    BlogPostDetailsView, BlogPostEditView

urlpatterns = (
    # Home
    path('', HomeView.as_view(), name='home'),

    # Posts
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('post-details/<int:pk>/', PostDetailsView.as_view(), name='post-details'),
    path('posts/', create_post_view, name='posts list'),

    # Blog Posts
    path('blog-post-details/<int:pk>/', BlogPostDetailsView.as_view(), name='blog-post-details'),
    path('blog-posts/', create_blog_post_view, name='blog-posts-list'),
    path('edit-blog-post/<int:pk>/', BlogPostEditView.as_view(), name='edit-blog-post'),

    # Loading BlogPosts and Posts with button
    path('data/<int:num_posts>/', load_post_data_view, name='post-data'),
    path('blog-data/<int:num_blog_posts>/', load_blog_post_data_view, name='blog-post-data'),

    # Like and Unlike post
    path('like-unlike-post/', like_unlike_post_view, name='like-unlike-post'),
)
