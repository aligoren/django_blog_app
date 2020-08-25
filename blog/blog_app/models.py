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
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    # when global comment setting is on, this field will be available
    comments_enabled = models.BooleanField(default=True)
    
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode.unidecode(self.title))
        
        return super().save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    # when global comment setting is on, this field will be available
    comments_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode.unidecode(self.title))
        return super().save(*args, **kwargs)


class Setting(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    
    posts_per_page = models.IntegerField(default=10)

    # this overrides all post and page comment options
    comments_enabled = models.BooleanField(default=True)

    comments_needs_approval = models.BooleanField(default=False)

    post_permalink = models.CharField(max_length=100, default="%postname%")