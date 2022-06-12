from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>', login_required(views.UserProfile.as_view()), name='user_profile'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),

]