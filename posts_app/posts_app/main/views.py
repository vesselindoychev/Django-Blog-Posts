from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from posts_app.main.forms import CreatePostForm
from posts_app.main.models import Post


class HomeView(views.TemplateView):
    template_name = 'main/home.html'


class CreatePostView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'main/create_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # print(form.instance.user)
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, views.ListView):
    model = Post
    template_name = 'main/posts-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object_list.filter(user=self.request.user)
        # context['text'] = 'Hello world'

        return context


class PostDetailsView(views.DetailView):
    model = Post
    template_name = 'main/post-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.object.user_id == self.request.user.id
        return context


def load_post_data_view(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            'author': obj.user.email,
            'liked': True if request.user in obj.liked.all() else False,
            'likes_count': obj.like_count,
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})
