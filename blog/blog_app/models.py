from django.db import models
from django.template.defaultfilters import slugify

import unidecode

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode.unidecode(self.category_name))
        return super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode.unidecode(self.title))
        return super().save(*args, **kwargs)

