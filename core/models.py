from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField

# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField("email address", max_length=255, unique=True)
    image = ResizedImageField(
        size=[300, 300], default="default_user_image.webp", upload_to="profile_pics"
    )

    def __str__(self) -> str:
        return self.username
