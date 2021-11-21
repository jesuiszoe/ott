from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'review/post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post" : post }
    return render(request, 'review/post_detail.html', context)
