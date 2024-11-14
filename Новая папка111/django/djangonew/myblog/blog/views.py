from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Blog

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'post_list.html', {'blogs': blogs})
