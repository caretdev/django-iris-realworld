from __future__ import annotations

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(
        self, email: str, password: str | None = None, **other_fields
    ) -> User:

        user = User(email=email, **other_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self.db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):

    # remove default fields
    username = None
    first_name = None
    last_name = None

    email: str = models.EmailField("Email Address", unique=True)
    name: str = models.CharField(max_length=60)
    bio: str = models.TextField(blank=True)
    image: str | None = models.URLField(null=True, blank=True)

    followers = models.ManyToManyField("self", blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        return reverse("profile", args=[self.id])

    def get_full_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        return self.name
