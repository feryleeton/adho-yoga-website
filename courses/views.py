from django.views.generic import ListView, DetailView

from courses.models import Course, Lesson


class SingleCourse(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/course-single.html'
    slug_field = 'slug'
    slug_url_kwarg = 'course_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course__slug=self.kwargs.get('course_slug')).all()
        context['first_lesson'] = Lesson.objects.filter(course__slug=self.kwargs.get('course_slug')).all()[0]
        return context


class CoursesHome(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
