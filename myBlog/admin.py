from django.contrib import admin
from myBlog.models import BlogsPost


#Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']

admin.site.register(BlogsPost, BlogsPostAdmin)