from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post, Category, Comment


class Blog(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog.html'
    paginate_by = 9


class SingleBlog(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blog-single.html'
    slug_field = 'slug'
    slug_url_kwarg = 'art_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post__slug=self.kwargs.get('art_slug')).order_by('-published')
        context['form'] = CommentForm()

        return context


class SingleCategory(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'blog/category-single.html'
    slug_field = 'slug'
    slug_url_kwarg = 'cat_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category__slug=self.kwargs.get('cat_slug'))
        paginator = Paginator(context['posts'], 9)
        page_number = self.request.GET.get('page')
        print(page_number)
        context['page_obj'] = paginator.get_page(page_number)
        return context


@login_required
@require_http_methods(["POST"])
def comment_reply_handler(request, pk, *args, **kwargs):
    parent_comment = Comment.objects.get(pk=pk)
    post = Post.objects.get(pk=parent_comment.post.pk)

    form = CommentForm(request.POST)

    new_comment = form.save(commit=False)
    new_comment.user_id = request.user.pk
    new_comment.post = post
    new_comment.parent = parent_comment
    new_comment.save()

    return redirect('blog_single', post.slug)


@login_required
@require_http_methods(["POST"])
def send_comment_handler(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        user = request.user
        content = request.POST['message']

        comment = Comment.objects.create(user=user, message=content, post_id=pk)
        comment.save()

        post = Post.objects.get(pk=pk)

    return redirect('blog_single', post.slug)


def search_request_handler(request):
    search_query = request.GET['q']
    posts = Post.objects.filter(title__icontains=search_query.strip().lower())
    return render(request, 'blog/search_result.html', {
        'posts': posts,
        'search_query': search_query,
    })
