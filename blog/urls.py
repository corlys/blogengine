from .views import *

from django.urls import path

urlpatterns = [
    # path("", PostList.as_view(), name="home"),
    # path("<slug:slug>", PostDetail.as_view(), name="post_detail"),
    path("", post_list, name="home"),
    path("post/create", PostCreate.as_view(), name="post_create"),
    path("post/<str:slug>/update", PostUpdate.as_view(), name="post_update"),
    path("post/<str:slug>/delete", PostDelete.as_view(), name="post_delete"),
    path("post/<str:slug>", PostDetail.as_view(), name="post_detail"),
    path("tags/", tags_list, name="tags_list"),
    path("tags/create", TagCreate.as_view(), name="tags_create"),
    path("tags/<str:slug>", TagDetail.as_view(), name="tags_detail"),
    path("tags/<str:slug>/update", TagUpdate.as_view(), name="tags_update"),
    path("tags/<str:slug>/delete", TagDelete.as_view(), name="tags_delete"),
]
