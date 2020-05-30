from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

class Forex(models.Model):
    topic = models.CharField(max_length=100, unique=False, null=False)
    content = models.TextField(max_length=4096, null=False)
    source = models.URLField(null=False)
    published = models.DateTimeField(auto_now=True, null=False)
    img = models.FileField(upload_to='upload/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Stock(models.Model):
    topic = models.CharField(max_length=100, unique=False, null=False)
    content = models.TextField(max_length=4096, null=False)
    source = models.URLField(null=False)
    published = models.DateTimeField(auto_now=True, null=False)
    img = models.FileField(upload_to='upload/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Commodity(models.Model):
    topic = models.CharField(max_length=100, unique=False, null=False)
    content = models.TextField(max_length=4096, null=False)
    source = models.URLField(null=False)
    published = models.DateTimeField(auto_now=True, null=False)
    img = models.FileField(upload_to='upload/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Crypto(models.Model):
    topic = models.CharField(max_length=100, unique=False, null=False)
    content = models.TextField(max_length=4096, null=False)
    source = models.URLField(null=False)
    published = models.DateTimeField(auto_now=True, null=False)
    img = models.FileField(upload_to='upload/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
