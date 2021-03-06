from django.urls import path
from .views import ArticleAPIView, ArticleDetail

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>', ArticleDetail.as_view()),
]
