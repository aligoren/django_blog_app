from django.contrib import admin

from .models import Post, Page, Category, Setting


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug', )

class PageAdmin(admin.ModelAdmin):
    exclude = ('slug', )

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug', )


admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Setting)