from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    image = models.ImageField(upload_to='blog/' , default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    content = models.TextField()
    title = models.CharField(max_length=201)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    

    class Meta:
        ordering = ['created_date']

        




