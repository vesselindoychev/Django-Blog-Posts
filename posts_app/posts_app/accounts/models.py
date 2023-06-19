import datetime

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


class Country(models.Model):
    COUNTRY_MAX_LENGTH = 30
    COUNTRY_MIN_LENGTH = 5

    name = models.CharField(
        max_length=COUNTRY_MAX_LENGTH,
        validators=(
            MinLengthValidator(COUNTRY_MIN_LENGTH),
        )
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


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

    # BULGARIA = 'Bulgaria'
    # FRANCE = 'France'
    # ITALY = 'Italy'
    # GREECE = 'Greece'
    #
    # COUNTRIES = (
    #     BULGARIA, ITALY, FRANCE, GREECE
    # )

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

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    location = models.TextField(
        null=True,
        blank=True
    )

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

    # Username, City, Country

    def __str__(self):
        return f" Profile of the user {self.user.email}"

    def bio_as_list(self):
        return self.bio.split('\n')

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_age(self):
        return datetime.datetime.now().year - self.date_of_birth.year
