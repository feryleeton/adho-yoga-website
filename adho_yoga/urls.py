from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('accounts.urls')),
    path('schedule/', include('schedule.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls'))
]