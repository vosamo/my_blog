from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, id):
    post = Article.objects.get(id=str(id))
    # str = "title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content)
    return render(request, 'post.html', {'post': post})
