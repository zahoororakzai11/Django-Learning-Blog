import os
import django
from django.utils import timezone  # Correct import for timezone

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
django.setup()

from authentications.models import *

# Creating multiple User records
users_data = [
    {"email": "user1@example.com", "password": "password1"},
    {"email": "user2@example.com", "password": "password2"},
    {"email": "user3@example.com", "password": "password3"},
]

users = []
for user_data in users_data:
    user = User.objects.create(
        email=user_data["email"],
        password=user_data["password"],
        is_staff=True,
        is_active=True,
        is_admin=False,
        otpauth_url="https://example.com/otpauth",
        otp_base32="base32string",
        login_otp="123456",
        login_otp_used=False,
        otp_created_at=timezone.now(),  # Correct way to get current time with timezone
    )
    users.append(user)

# Creating multiple Author records
authors_data = [
    {"name": "Author One"},
    {"name": "Author Two"},
    {"name": "Author Three"},
]

authors = []
for author_data in authors_data:
    author = Author.objects.create(name=author_data["name"])
    authors.append(author)

# Creating multiple Post records
posts_data = [
    {
        "title": "Post One",
        "content": "Content of Post One.",
        "authors": [authors[0], authors[1]],
    },
    {
        "title": "Post Two",
        "content": "Content of Post Two.",
        "authors": [authors[1], authors[2]],
    },
    {
        "title": "Post Three",
        "content": "Content of Post Three.",
        "authors": [authors[0]],
    },
]

posts = []
for post_data in posts_data:
    post = Post.objects.create(
        title=post_data["title"],
        content=post_data["content"],
        published_date=timezone.now(),  # Corrected here as well
    )
    post.author.set(post_data["authors"])
    posts.append(post)

persons_data = [
    {"name": "Alice", "shirt_size": "S"},
    {"name": "Bob", "shirt_size": "M"},
    {"name": "Charlie", "shirt_size": "L"},
    {"name": "Diana", "shirt_size": "M"},
    {"name": "Eve", "shirt_size": "S"},
]

# Creating Person records
persons = []
for person_data in persons_data:
    person = Person.objects.create(
        name=person_data["name"],
        shirt_size=person_data["shirt_size"],
    )
    persons.append(person)

# Print the created records
print(f"Persons: {[str(person) for person in persons]}")
print(f"Users: {[str(user) for user in users]}")
print(f"Authors: {[str(author) for author in authors]}")
print(f"Posts: {[str(post) for post in posts]}")
