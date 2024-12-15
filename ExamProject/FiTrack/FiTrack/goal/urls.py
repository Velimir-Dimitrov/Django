from django.urls import path
from .views import GoalListView, GoalDetailView, GoalCreateView

urlpatterns = [
    path('', GoalListView.as_view(), name='goal-list'),
    path('<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('create/', GoalCreateView.as_view(), name='goal-create'),
]