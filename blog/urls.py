from django.conf.urls.static import static
from django.urls import path

from adho_yoga import settings
from . import views

urlpatterns = [
    path('', views.Blog.as_view(), name='blog'),
    path('post/<slug:art_slug>/', views.SingleBlog.as_view(), name='blog_single'),
    path('category/<slug:cat_slug>/', views.SingleCategory.as_view(), name='category'),
    path('add_comment_reply/<int:pk>/', views.comment_reply_handler, name='add_comment_reply'),
    path('send_comment/<int:pk>', views.send_comment_handler, name='send_comment'),
    path('search_posts', views.search_request_handler, name='search_posts'),
]
