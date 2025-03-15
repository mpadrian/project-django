from django.shortcuts import render
from django.views.generic import ListView
from post.models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post.html'

def postList(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post.html', context)
    
