from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from posts_app.accounts.managers import PostsAppUserManager
from posts_app.common.custom_validators import validate_only_letters, validate_first_letter_to_be_capital


class PostsAppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = PostsAppUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 2
    UPLOAD_TO_DIR = 'avatars/'

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    SEX_GROUPS = (
        MALE,
        FEMALE,
        OTHER,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
            validate_first_letter_to_be_capital,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
            validate_first_letter_to_be_capital,
        ),
    )

    avatar = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
    )

    sex = models.CharField(
        max_length=(max(len(s) for s in SEX_GROUPS)),
        choices=((s, s) for s in SEX_GROUPS),
    )

    date_of_birth = models.DateField()

    updated = models.DateTimeField(
        auto_now=True,
    )

    created = models.DateField(
        auto_now_add=True,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        PostsAppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.user.email
    