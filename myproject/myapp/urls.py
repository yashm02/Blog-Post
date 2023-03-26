from django.urls import path
from .views import BlogPostList, BlogPostDetail

urlpatterns = [
    path('create/', BlogPostList.as_view(), name='blogpost-list'),
    path('create/<int:pk>/', BlogPostDetail.as_view(), name='blogpost-detail'),
    path('all/', BlogPostList.as_view(), name='blogpost-list'),
]
