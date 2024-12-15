from django.urls import path, include
from .views import (
    WorkoutListView,
    WorkoutDetailView,
    WorkoutCreateView,
    WorkoutUpdateView,
    WorkoutDeleteView
)

urlpatterns = [
    path('', WorkoutListView.as_view(), name='workout-list'),
    path('create/', WorkoutCreateView.as_view(), name='workout-create'),
    path('<int:user_id>/workout/<int:pk>/', include([
        path('', WorkoutDetailView.as_view(), name='workout-detail'),
        path('update/', WorkoutUpdateView.as_view(), name='workout-update'),
        path('delete/', WorkoutDeleteView.as_view(), name='workout-delete'),
    ])),
]