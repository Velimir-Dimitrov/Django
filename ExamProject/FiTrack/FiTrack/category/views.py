from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .forms import CategoryForm
from .models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category-list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category-add-edit.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category-add-edit.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')