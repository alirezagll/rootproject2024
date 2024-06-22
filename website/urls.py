from django.urls import path
from website.views import  func_index ,func_elements ,func_contact ,func_about

app_name = 'website'

urlpatterns = [

    path('',func_index,name='index'),
    path('about',func_about,name='about'),
    path('contact',func_contact,name='contact'),
    path('elements',func_elements,name='elements'),

]



