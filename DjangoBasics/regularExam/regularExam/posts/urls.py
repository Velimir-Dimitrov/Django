from django.urls import path, include

from regularExam.posts.views import PostCreateView, PostDetailsViews, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:id>/', include([
        path('details/', PostDetailsViews.as_view(), name='post-details'),
        path('edit/', PostEditView.as_view(), name='post-edit'),
        path('delete/', PostDeleteView.as_view(), name='post-delete')]
    ))
]