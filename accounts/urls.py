from django.conf.urls.static import static
from django.urls import path

from adho_yoga import settings
from . import views


urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),

]