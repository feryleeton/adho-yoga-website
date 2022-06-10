from django.conf.urls.static import static
from django.urls import path

from adho_yoga import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('classes/', views.classes, name='classes'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
