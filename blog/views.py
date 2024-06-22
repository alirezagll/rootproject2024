from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from blog.models import Posts





def func_blog_home(request):
    return render(request,'blog-home.html')


def func_blog_single(request):
    return render(request,'blog-single.html')

def func_blog(request):
    return HttpResponse('<h2 style="color=blue">hello welcome to blog  </h2>')


def func_test(request):
    now = timezone.now()
    posts = Posts.objects.filter(published_date__lte=now , status=True)
    context = {'posts':posts}
    return render(request,'blog-home.html', context)


def post_detail(request, pid):
    post = Posts.objects.filter(status=True)
    post = get_object_or_404(Posts, pk=pid )
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog-single.html', context)
