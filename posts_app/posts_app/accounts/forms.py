import datetime

from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from posts_app.accounts.models import Profile

UserModel = get_user_model()


class CreateProfileForm(auth_forms.UserCreationForm):
    YEARS = [i for i in range(1980, int(datetime.datetime.now().year + 1))]
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'First name'}
        )
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last name'},
        ),
    )

    sex = forms.CharField(
        widget=forms.Select(
            choices=((s, s) for s in Profile.SEX_GROUPS)
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': f'{10 * "*"}'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': f'{10 * "*"}'})

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            sex=self.cleaned_data['sex'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'sex',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'gosho@gmail.com'
                },
            ),
        }
