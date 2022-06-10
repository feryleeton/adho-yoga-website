from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'created']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['user',
                    'published']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)