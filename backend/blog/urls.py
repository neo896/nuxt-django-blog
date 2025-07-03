from django.urls import path
from .views import CategoryView, ArticleView

urlpatterns = [
    path("category/", CategoryView.as_view(), name="category"),
    path("article/", ArticleView.as_view(), name="article"),
]
