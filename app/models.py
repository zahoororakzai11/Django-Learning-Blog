from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} profile"


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField()

    us_gross = models.IntegerField(default=0)
    worldwide_gross = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class Resource(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
