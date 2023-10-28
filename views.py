from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost, 

from .forms import CommentForm  

@login_required
def my_protected_view(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment was posted successfully.')
            return redirect('my_protected_view')

    blog_posts = BlogPost.objects.all()
    comment_form = CommentForm()

    return render(request, 'protected_view.html', {'blog_posts': blog_posts, 'comment_form': comment_form})
