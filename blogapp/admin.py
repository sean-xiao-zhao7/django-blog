from blogapp.models import Author, Post, Tag, Comment
from django.contrib import admin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date',)
    list_display = ('title', 'author', 'date',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
