from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.articles, name="articles"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
]
