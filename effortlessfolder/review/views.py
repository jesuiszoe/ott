from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'review/post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post" : post}
    return render(request, 'review/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        new_post = Post(
            title = title,
            content = content
        )
        new_post.save()
        return redirect('review:post-detail', post_id = new_post.id )

    else:
        post_form = PostForm()
        return render(request, 'review/post_form.html', {'form' : post_form})


    
    