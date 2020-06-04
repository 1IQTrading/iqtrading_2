from django.contrib import admin

from .models import Category, Post

# admin.site.register(Category)
# admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')




