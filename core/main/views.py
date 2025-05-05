from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import AutomobileImage
from main.forms import FeedBackRequestModelForm
from main.models import BannerModel
from posts.models import PostModel
from utils.split_content import split_content


def index(request) -> HttpResponse:
    modal_active: bool = False
    sent_feedback: bool = False
    form = FeedBackRequestModelForm()
    if request.method == "POST":
        modal_active = True
        form = FeedBackRequestModelForm(request.POST)
        if form.is_valid():
            new_feedback_request = form.save(commit=False)
            new_feedback_request.save()
            sent_feedback = True
            modal_active = False
            form = FeedBackRequestModelForm()

    last_cars = AutomobileImage.objects.filter(position=0).select_related("automobile").order_by("automobile__created_at")[:10]
    last_cars_set = split_content(last_cars, 4)
    posts = PostModel.objects.order_by("created_at")[:8]
    posts_set = split_content(posts, 4)
    banners = BannerModel.objects.order_by("position")
    return render(
        request,
        "core/index.html",
        context={
            "cars": last_cars_set,
            "banners": banners,
            "posts": posts_set,
            "form": form,
            "modal_active": modal_active,
            "sent_feedback": sent_feedback,
        }
    )


def about_us(request) -> HttpResponse:
    return render(request, "core/about_us.html")


def contacts(request) -> HttpResponse:
    return render(request, "core/contacts.html")
