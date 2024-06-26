from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import Post

def index(request):
    return render(request, "home.html", context={"posts": Post.objects.all()})

def post_detail_view(request, post_id):
    post_detail = Post.objects.get(id=post_id)
    return render(request, "details.html", context={"post": post_detail})
