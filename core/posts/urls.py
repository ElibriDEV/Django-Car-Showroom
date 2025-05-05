from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('', views.posts, name="posts"),
    path('new', views.new_post, name="new-post"),
    path('<int:pk>', views.detail, name="post-detail"),
    path('<int:pk>/<int:comment_pk>', views.delete_comment, name="comment-delete"),

]