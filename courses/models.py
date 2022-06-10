from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image_preview = models.ImageField(upload_to='courses_previews/%Y/%m/%d', verbose_name='Превью курса')
    description = RichTextUploadingField(verbose_name='Описание')
    created = models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='Дата \ Время создания')
    slug = models.SlugField(verbose_name='Slug-ссылка')
    paid = models.BooleanField(default=False, verbose_name='Платный')

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    video = models.FileField(upload_to='lesson_videos/%Y/%m/%d', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Видеоматериал')
    image_preview = models.ImageField(upload_to='lesson_previews/%Y/%m/%d', null=True, verbose_name='Видео превью')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title