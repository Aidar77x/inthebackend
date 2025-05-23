from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Список тредов
def thread_list(request):
    threads = Thread.objects.all()
    form = ThreadForm()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

# Детали треда + посты
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

# Удаление треда
def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

# Редактирование треда
def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    form = ThreadForm(instance=thread)
    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    return render(request, 'post/thread_edit.html', {'form': form})

# Удаление поста
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

# Редактирование поста
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    return render(request, 'post/post_edit.html', {'form': form})
