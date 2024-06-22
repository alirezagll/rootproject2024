from django.shortcuts import render
from django.utils import timezone
#from website.models import Posts 

def func_index(request):
    return render(request,'index.html')

def func_about(request):
    return render(request,'about.html')

def func_contact(request):
    return render(request,'contact.html')

def func_elements(request):
    return render(request,'elements.html')
#
#def func_test(request):
#    now = timezone.now()
#    posts = Posts.objects.filter(published_date__lte=now)
#    context = {'posts':posts}
#    return render(request,'test.html', context)
#