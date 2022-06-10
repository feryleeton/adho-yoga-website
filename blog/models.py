from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug-ссылка')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title', ]

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='Slug-ссылка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='post_images/%Y/%m/%d', blank=True, verbose_name='Превью')
    text = RichTextUploadingField(verbose_name='Текст')
    created = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Дата \ Время создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Комментарий')
    published = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Дата \ Время публикации')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+', verbose_name='Ответ на')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('published', )

    def __str__(self):
        return self.message

    @property
    def has_replies(self):
        if self.parent:
            return False
        else:
            return True