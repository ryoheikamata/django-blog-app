from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    CategoryPostLisstView,
    TagPostListView,
    SearchPosListView,
    CommentCreateView,
    CommentDeleteView,
    ReplyCreateView,
    ReplyDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/<str:slug>/', CategoryPostLisstView.as_view(), name='category-post-list'),
    path('tag/<str:slug>/', TagPostListView.as_view(), name='tag-post-list'),
    path('search/', SearchPosListView.as_view(), name='search-post-list'),
    path('comment/<int:post_pk>/', CommentCreateView.as_view(), name='comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('reply/<int:comment_pk>/', ReplyCreateView.as_view(), name='reply'),
    path('reply/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply-delete'),
]



