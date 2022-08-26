from django.db import models
from account.models import User

from autoslug import AutoSlugField

choices = [("D", "Draft"), ("P", "Published")]


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


# class Author(models.Model):
# user_key=models.ForeignKey(User,on_delete=models.CASCADE)

# def __str__(self):
# return self.user_key.username


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2, choices=choices, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True
    )
