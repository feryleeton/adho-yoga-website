from django import template
from blog.models import Post, Comment

register = template.Library()


@register.inclusion_tag('blog/tags_templates/display_date.html')
def display_date(date_created):
    date_list = date_created.strftime('%B/%d/%Y').split(' ')[0].split('/')
    day = date_list[1]
    month = date_list[0]
    year = date_list[2]
    return {"day": day, "month": month, "year": year}


@register.inclusion_tag('blog/tags_templates/display_recent_blog.html')
def display_recent_blog():
    recent_blog = Post.objects.all().order_by('-id')
    if len(recent_blog) > 3:
        last_articles = recent_blog[:3]
    else:
        last_articles = recent_blog
    return {'last_articles': last_articles}


@register.inclusion_tag('blog/tags_templates/display_reply_form.html')
def display_reply_form(comment, form):
    return {'comment': comment,
            'form': form}


@register.inclusion_tag('blog/tags_templates/display_replies.html')
def display_replies(comment):
    replies = Comment.objects.filter(parent=comment.pk).all()
    return {'replies': replies, }


@register.inclusion_tag('blog/tags_templates/display_comments_count.html')
def display_comments_count(post):
    comments = Comment.objects.filter(post=post.pk).all()
    return {'post_comments': comments}


@register.inclusion_tag('blog/tags_templates/display_posts_count.html')
def display_posts_count(category):
    posts = Post.objects.filter(category=category.pk).all()
    return {'posts': posts}