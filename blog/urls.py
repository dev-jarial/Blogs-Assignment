from django.urls import path
from .views import home_view, blog_list, blog_detail, create_blog_post, blog_update
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home_view, name='home'),
    path('blog-list', blog_list, name='blog_list'),
    path('post/new/', create_blog_post, name='create_blog_post'),
    path('post/<int:pk>/', blog_detail, name='blog_detail'),
    path('post/<int:pk>/edit/', blog_update, name='blog_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)