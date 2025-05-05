from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    path('', views.catalog, name="catalog"),
    path('<int:pk>', views.detail, name="detail"),
]
