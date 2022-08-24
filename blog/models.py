
from django.db import models
from django.contrib.auth.models import User

from autoslug import AutoSlugField

class Author(models.Model):
    user_key=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_key.username    

class Post(models.Model):
    title = models.CharField(max_length=150,unique=True)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='posts')

