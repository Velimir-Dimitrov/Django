from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .forms import CategoryForm
from .models import Category

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/category-list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category-add-edit.html'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        if not self.request.user.is_superuser:
            raise Http404("Page not found.")
        return True


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category-add-edit.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        if not self.request.user.is_superuser:
            raise Http404("Page not found.")
        return True