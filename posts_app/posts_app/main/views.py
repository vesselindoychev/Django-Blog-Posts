from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from posts_app.accounts.models import Profile
from posts_app.main.forms import CreatePostForm, CreateBlogForm, EditBlogForm
from posts_app.main.models import Post, Blog

UserModel = get_user_model()


class HomeView(views.TemplateView):
    template_name = 'main/home.html'


class CreatePostView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'main/create_post.html'
    success_url = reverse_lazy('create-post')

    def form_valid(self, form):
        # print(form.instance.user)\
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


class BlogPostDetailsView(views.DetailView):
    model = Blog
    template_name = 'main/blog-post-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.object.user_id == self.request.user.id
        context['edit_form'] = EditBlogForm
        return context


class BlogPostEditView(views.UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'main/edit-blog-post.html'

    def get_success_url(self):
        return reverse_lazy('blog-post-details', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.object.user_id == self.request.user.id
        return context


def create_blog_post_view(request):
    form = CreateBlogForm(request.POST or None)

    if request.is_ajax():
        if form.is_valid():
            creator = Profile.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.user = creator
            instance.save()
            return JsonResponse({
                'title': instance.title,
                'body': instance.body,
                'author': instance.user.user.email,
                'id': instance.id,
            })

    context = {
        'form': form,
    }

    return render(request, 'main/blog-posts-list.html', context)


def edit_blog_post_view(request, pk):
    global new_title, new_body
    obj = Blog.objects.get(pk=pk)
    if request.is_ajax():
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        obj.title = new_title
        obj.body = new_body
        obj.save()
    return JsonResponse({
        'title': new_title,
        'body': new_body,
    })


def delete_blog_post_view(request, pk):
    obj = Blog.objects.get(pk=pk)
    if request.is_ajax():
        obj.delete()
    return JsonResponse({})


def create_post_view(request):
    form = CreatePostForm(request.POST or None)

    if request.is_ajax():
        if form.is_valid():
            creator = Profile.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.user = creator
            instance.save()

    context = {
        'form': form,
    }

    return render(request, 'main/posts-list.html', context)


def load_post_data_view(request, num_posts):
    if request.is_ajax():
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
                'is_creator': obj.user == request.user
            }
            data.append(item)
        return JsonResponse({'data': data[lower:upper], 'size': size})


def load_blog_post_data_view(request, num_blog_posts):
    if request.is_ajax():
        visible = 3
        upper = num_blog_posts
        lower = upper - visible
        size = Blog.objects.all().count()
        qs = Blog.objects.all()

        data = []

        for obj in qs:
            item = {
                'id': obj.id,
                'title': obj.title,
                'body': obj.body,
                'author': obj.user.user.email,
                'liked': True if obj.user in obj.liked.all() else False,
                'likes_count': obj.like_count,
                'is_creator': obj.user.user == request.user
            }
            data.append(item)
        return JsonResponse({'data': data[lower:upper], 'size': size})


def like_unlike_post_view(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)

        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)

        return JsonResponse({'liked': liked, 'likes_count': obj.like_count})
