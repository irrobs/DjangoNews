from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm

# Create your views here.
from blog.models import Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Define o autor como o usuário logado
            post.save()
            return redirect(home)  # Substitua por uma URL válida
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})