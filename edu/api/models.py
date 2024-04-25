from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    # name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200)
    file = models.FileField(upload_to='media/')
    description = models.TextField(blank=True)
    # category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
  


