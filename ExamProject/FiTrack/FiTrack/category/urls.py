from django.urls import path

from FiTrack.category.views import CategoryListView, CategoryCreateView, CategoryUpdateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('add/', CategoryCreateView.as_view(), name='add_category'),
    path('edit/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
]