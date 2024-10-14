from django.shortcuts import render
from .models import Post
from .forms import PostForm


def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'Post/templates/post/post_form.html', context)


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'Post/templates/post/home.html', context)


def about(request):
    return render(request, 'Post/templates/blog/about.html')