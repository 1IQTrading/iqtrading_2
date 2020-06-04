from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    about = models.TextField(max_length=100, unique=False, null=False)
    content = models.TextField(max_length=4096, unique=False, null=False)
    image = models.FileField(null=False, upload_to='upload/')
    published = models.DateTimeField(null=False, default=datetime.now().replace(microsecond=0))
    source = models.URLField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

