import uuid
from datetime import datetime, date
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from authentications.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), null=True, blank=True, unique=True)
    password = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    otpauth_url = models.CharField(max_length=225, blank=True, null=True)
    otp_base32 = models.CharField(max_length=255, null=True)
    login_otp = models.CharField(max_length=255, null=True, blank=True)
    login_otp_used = models.BooleanField(default=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.email

    def is_valid_otp(self):
        lifespan_in_seconds = 30
        now = datetime.now(timezone.utc)
        time_diff = now - self.otp_created_at
        time_diff = time_diff.total_seconds()
        if time_diff >= lifespan_in_seconds or self.login_otp_used:
            return False
        return True


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ManyToManyField(Author, related_name="posts")

    def __str__(self) -> str:
        return self.title


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    hometown = models.ForeignKey(
        "City",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through="Membership")

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Course(models.Model):
    name  = models.CharField(max_length=20)
    student  = models.ManyToManyField("Student")
    
    def __str__(self):
        return "%s(%s)"%(self.name,''.join(student.name for student in self.student.all()))
    
class Student(CommonInfo):
    student = models.CharField(max_length=20)

    class Meta(CommonInfo.Meta):
        db_table = "student_info"

class City(models.Model):
    name = models.CharField(max_length=100,null=True)

class Book(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)


# ************************* Proxy Model Concept ********************************
class MyPerson(Person):
    class Meta:
        ordering = ["name"]
        proxy = True

    def do_something(self):
        pass


# proxy model order will be on name, but other models will be unorder
class OrderedPerson(Person):
    class Meta:
        ordering = ["name"]
        proxy = True
        
        
class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )