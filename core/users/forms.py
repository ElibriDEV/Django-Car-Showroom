from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms as f
from django.contrib.auth.models import User


class AuthUserForm(AuthenticationForm, f.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Имя пользователя:"
        self.fields["username"].widget = f.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["password"].label = "Пароль:"
        self.fields["password"].widget = f.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Имя пользователя:"
        self.fields["username"].widget = f.TextInput(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["password1"].label = "Пароль:"
        self.fields["password1"].widget = f.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["password2"].label = "Подтвердите пароль:"
        self.fields["password2"].widget = f.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )


class UserUpdateForm(f.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["username"].help_text = ""
        self.fields["username"].widget = f.TextInput(
            attrs={
                "placeholder": "Имя пользователя",
                "class": "form-control",
            }
        )
        self.fields["first_name"].label = ""
        self.fields["first_name"].help_text = ""
        self.fields["first_name"].widget = f.TextInput(
            attrs={
                "placeholder": "Имя",
                "class": "form-control",
            }
        )
        self.fields["last_name"].label = ""
        self.fields["last_name"].help_text = ""
        self.fields["last_name"].widget = f.TextInput(
            attrs={
                "placeholder": "Фамилия",
                "class": "form-control",
            }
        )
        self.fields["email"].label = ""
        self.fields["email"].help_text = ""
        self.fields["email"].widget = f.TextInput(
            attrs={
                "placeholder": "Электронная почта",
                "class": "form-control",
            }
        )