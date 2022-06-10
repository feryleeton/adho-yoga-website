from django.contrib import admin
from courses.models import Course, Lesson


class LessonAdmin(admin.StackedInline):
    extra = 1
    model = Lesson


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['title', 'created', ]
    inlines = [LessonAdmin, ]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Course, CourseAdmin)
