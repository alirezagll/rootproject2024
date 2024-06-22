from django.contrib import admin
from blog.models import Posts


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ["title", "status", "published_date","created_date",]





admin.site.register(Posts , PostAdmin)