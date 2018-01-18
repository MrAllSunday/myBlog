from django.shortcuts import render
from myBlog.models import BlogsPost


#Create your views here.

def blog_index(request):
    blog_list = BlogsPost.objects.all() #获取所有数据
    return render(request, 'index.html', {'blog_list':blog_list}) #返回所有页面index2.html