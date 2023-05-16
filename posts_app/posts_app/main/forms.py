from django import forms

from posts_app.main.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('user', )