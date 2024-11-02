from django.urls import path, include

from forumApp.posts import views
from forumApp.posts.views import Index, DashboardView, RedirectHomeView, AddPostView, EditPostView, DeletePostView, \
    DetailsPostView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("add-post/", AddPostView.as_view(), name="add-post"),
    path("<int:pk>/", include([
        path("delete-post/", DeletePostView.as_view(), name="delete-post"),
        path("edit-post/", EditPostView.as_view(), name="edit-post"),
        path("details-post/", DetailsPostView.as_view(), name="details-post"),
    ])),
    path("redirect-home/", RedirectHomeView.as_view(), name="redirect-home"),
]