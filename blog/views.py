from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def home_view(request):
    return render(request, 'blog/home.html')


def blog_list(request):
    query = request.GET.get('q')
    if query:
        blog_posts = BlogPost.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        blog_posts = BlogPost.objects.all().order_by('-created_at')
    
    paginator = Paginator(blog_posts, 5)  # Show 5 blog posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj, 'query': query})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/update_blog_post.html', {'form': form})