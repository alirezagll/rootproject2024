from django.urls import path
from blog.views import func_blog_home , func_blog_single , func_blog , func_test
from . import views




app_name = 'blog'

urlpatterns = [
    path('',func_blog),
    path('home',func_test,name='blog-home'),
    path('post/<int:pid>/',views.post_detail,name='blog-single'),
    #path(, views.post_detail, name='post-detail'),
    


]