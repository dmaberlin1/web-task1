from django.contrib import admin
from .models import News


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'theme', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('title', 'content', 'author')


admin.site.register(News, NewsAdmin)
