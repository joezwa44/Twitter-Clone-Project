from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


# Create your views here.


def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    # If the form is valid
        if form.is_valid():
          # Yes, save
            form.save()
            return HttpResponseRedirect('/')

        else:
          # No, show error
            return HttpResponseRedirect(form.erros.as_json())

    posts = Post.objects.all().order_by("-created_at")[:40]

    return render(request, 'posts.html', {'posts': posts})


def delete(request, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    posts = Post.objects.get(id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
          return HttpResponseRedirect("not valid")
    
    
    return render(request, 'edit.html', {'posts': posts})


def likes(request, post_id):
    posts = Post.objects.get(id=post_id)
    x= posts.likes + 1
    posts.likes=x
    posts.save()
    return HttpResponseRedirect('/')