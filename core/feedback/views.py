from django.http import HttpResponse
from django.shortcuts import render, redirect

from feedback.forms import FeedbackCreationForm


def feedback(request) -> HttpResponse:
    if request.method == "POST":
        form = FeedbackCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "feedback/feedback.html", context={'form_data': form.cleaned_data})
    else:
        form = FeedbackCreationForm()
    return render(request, "feedback/feedback.html", context={"form": form})
