from django.shortcuts import render,get_object_or_404
from .models import BlogModel

def all_blogs(request):
    blogs = BlogModel.objects.order_by('-date')
    return render(request,'all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(BlogModel,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})