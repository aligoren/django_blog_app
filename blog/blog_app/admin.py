from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug', )

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)