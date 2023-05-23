from django import forms

from posts_app.main.models import Post, Blog


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ('title', 'body',)


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body',)
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'rows': 5,
                }
            )
        }