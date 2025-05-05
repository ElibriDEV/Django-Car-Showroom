import datetime as dt

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests import Request

from posts.forms import CommentCreationForm, PostCreationForm
from posts.models import PostModel, CommentModel


def posts(request: Request) -> HttpResponse:
    posts = PostModel.objects.order_by("-created_at")
    page = int(request.GET.get("page"))
    paginator = Paginator(posts, 10)
    return render(request, "posts/posts.html", context={"page_data": paginator.page(page)})


@staff_member_required
def new_post(request) -> HttpResponse:
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("posts:post-detail", pk=new_post.pk)
    else:
        form = PostCreationForm()
    return render(request, "posts/new-post.html", context={"form": form})


def detail(request: Request, pk: int) -> HttpResponse:
    post = PostModel.objects.filter(pk=pk).first()
    comments = CommentModel.objects.filter(post=post).order_by("-created_at").all()
    if request.method == "POST":
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            return redirect("posts:post-detail", pk=pk)
    else:
        form = CommentCreationForm()

    return render(request, "posts/single-post.html", context={"post": post, "form": form, "comments": comments})


@login_required()
def delete_comment(request, pk: int, comment_pk: int):
    comment = CommentModel.objects.filter(pk=comment_pk).first()
    if comment.author == request.user:
        comment.delete()
        return redirect("posts:post-detail", pk=pk)
