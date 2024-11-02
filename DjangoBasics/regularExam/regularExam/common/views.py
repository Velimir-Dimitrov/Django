from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from regularExam.posts.models import Post
from regularExam.posts.views import PostEditView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/index.html'

class DashboardView(ListView):
    model = Post
    template_name = 'common/dashboard.html'


