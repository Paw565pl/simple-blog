from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)
from django.forms import FileInput, ImageField, ModelForm
from hcaptcha_field import hCaptchaField


class UserRegisterForm(UserCreationForm):
    hcaptcha = hCaptchaField(theme="dark")

    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class CustomAuthenticationForm(AuthenticationForm):
    hcaptcha = hCaptchaField(theme="dark")


class UserUpdateForm(ModelForm):
    image = ImageField(widget=FileInput)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "image"]
