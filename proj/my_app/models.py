from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    posted_at = models.DateTimeField(auto_now_add=True)