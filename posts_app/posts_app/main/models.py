from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from posts_app.accounts.models import Profile
from posts_app.common.custom_validators import validate_letters_numbers_space_and_dash

UserModel = get_user_model()


class BlogPost(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 5

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
            validate_letters_numbers_space_and_dash,
        )
    )

    body = models.TextField()

    liked = models.ManyToManyField(
        UserModel,
        blank=True,
        related_name='blog_liked',
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def like_count(self):
        # liked_post_by_user = Post.objects.get(user__in=self.liked)
        # total_likes = liked_post_by_user.liked.all().count()
        # return total_likes
        return self.liked.all().count()


class Post(models.Model):
    TITLE_MAX_LENGTH = 100
    TITLE_MIN_LENGTH = 5

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
            validate_letters_numbers_space_and_dash,
        )
    )

    body = models.TextField()

    liked = models.ManyToManyField(
        UserModel,
        blank=True,
        related_name='post_liked',
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def like_count(self):
        # liked_post_by_user = Post.objects.get(user__in=self.liked)
        # total_likes = liked_post_by_user.liked.all().count()
        # return total_likes
        return self.liked.all().count()
