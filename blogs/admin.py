from django.contrib import admin

# Register your models here.

from .models import Author, Category, Tag, Blog

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profession', 'is_active')
    search_fields = ('full_name', 'profession')
    list_filter = ('created_at','updated_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', '')
    list_filter = ('created_at','updated_at')    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'status', 'created_at')
    search_fields = ('title', 'short_description', 'long_description')
    list_filter = ('created_at','updated_at')    

    