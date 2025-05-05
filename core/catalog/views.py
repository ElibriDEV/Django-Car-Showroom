from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from requests import Request

from catalog.models import AutomobileModel
from utils.split_content import split_content


def catalog(request: Request) -> HttpResponse:
    page = int(request.GET.get("page"))
    cars = AutomobileModel.objects.filter(sold=False).order_by("created_at").prefetch_related('images').all()
    paginator = Paginator(cars, 16)
    cars_set = split_content(paginator.page(1).object_list, 4)
    return render(request, "catalog/catalog.html", context={"page_data": paginator.page(page), "cars_set": cars_set})


def detail(request: Request, pk: int) -> HttpResponse:
    car = AutomobileModel.objects.filter(pk=pk).prefetch_related('images').first()
    return render(request, "catalog/detail.html", context={"car": car})
