from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Workout
from .forms import WorkoutForm

UserModel = get_user_model()

class WorkoutListView(ListView):
    model = Workout
    template_name = "workouts/workout-list.html"
    context_object_name = "workouts"

    def get_queryset(self):
        return Workout.objects.filter(account=self.request.user)

class WorkoutDetailView(DetailView):
    model = Workout
    template_name = "workouts/workout-details.html"
    context_object_name = "workout"

    def get_object(self, queryset=None):
        user = get_object_or_404(UserModel, id=self.kwargs['user_id'])
        return get_object_or_404(Workout, account=user, pk=self.kwargs['pk'])

class WorkoutCreateView(CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "workouts/workout-create-update.html"
    success_url = reverse_lazy('workout-list')

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = ['name', 'category', 'duration_minutes', 'calories_burned', 'date']
    template_name = "workouts/workout-create-update.html"

    def get_object(self, queryset=None):
        user = get_object_or_404(UserModel, id=self.kwargs['user_id'])
        return get_object_or_404(Workout, account=user, pk=self.kwargs['pk'])

class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = "workouts/workout-delete.html"
    success_url = reverse_lazy('workout-list')

    def get_object(self, queryset=None):
        user = get_object_or_404(UserModel, id=self.kwargs['user_id'])
        return get_object_or_404(Workout, account=user, pk=self.kwargs['pk'])