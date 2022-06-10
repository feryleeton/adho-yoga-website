from django import template
from blog.models import Post
import datetime

register = template.Library()


@register.inclusion_tag('main/tags_templates/display_recent_posts.html')
def display_recent_posts():
    recent_blog = Post.objects.all().order_by('-id')
    if len(recent_blog) > 3:
        last_articles = recent_blog[:3]
    else:
        last_articles = recent_blog
    return {'recent_posts': last_articles, }

