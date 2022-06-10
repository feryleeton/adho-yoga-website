from django.urls import path

from courses import views


urlpatterns = [
    path('', views.CoursesHome.as_view(), name='courses'),
    path('<slug:course_slug>', views.SingleCourse.as_view(), name='course_single'),
]