from django.views.generic import CreateView, DetailView, ListView
from rest_framework.reverse import reverse_lazy

from .forms import GoalForm
from .models import Goal

class GoalCreateView(CreateView):
    form_class = GoalForm
    template_name = "goals/goal-create.html"
    success_url = reverse_lazy('goal-list')

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

class GoalDetailView(DetailView):
    model = Goal
    template_name = "goals/goal-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goal = self.get_object()
        context['workouts'] = goal.workouts.all()
        context['progress'] = goal.progress()
        return context

class GoalListView(ListView):
    model = Goal
    template_name = "goals/goal-list.html"

    def get_queryset(self):
        return Goal.objects.filter(account=self.request.user)