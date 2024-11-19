import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, CreateView, UpdateView, DeleteView, FormView, \
    DetailView
from forumApp.decorators import measure_execution_time
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, PostEditForm, SearchForm, CommentFormSet
from forumApp.posts.mixins import TimeRestrictedMixin
from forumApp.posts.models import Post
from django.forms import modelform_factory


# Create your views here.

# # test basic Class View

# class BaseView:
#     @classonlymethod
#     def as_view(cls):
#
#         def view(request, *args, **kwargs):
#             view_instance = cls()
#             return view_instance.dispatch(request, *args, **kwargs)
#
#         return view
#
#     def dispatch(self, request, *args, **kwargs):
#         if request.method == "GET":
#             return self.get(request, *args, **kwargs)
#         elif request.method == "POST":
#             return self.post(request, *args, **kwargs)

# class Index(TemplateView):
#
#     # Static way to template
#     template_name = "common/index.html"
#
#     # dynamic
#     def get_template_names(self):
#         if self.request.user.is_authenticated:
#             return ["common/index.html", ]
#         else:
#             return ["common/login.html", ] #not created yet -> "TemplateDoesNotExist" error
#
#     # Static way to set context
#     extra_context = {'static_time': datetime.datetime.now()}
#
#     # dynamic
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["dynamic_time"] = datetime.datetime.now()
#         return context


@method_decorator(measure_execution_time, name='dispatch')
class Index(TimeRestrictedMixin, View):
    def get(self, request, *args, **kwargs):
        test_form_factory = modelform_factory(Post, fields=("title", "author", "languages"))

        context = {
            "test_form_factory": test_form_factory,
            "dynamic_time": datetime.datetime.now()
        }

        return render(request, "common/index.html", context)

# # function view
# def index(request):
#
#     test_form_factory = modelform_factory(Post, fields=("title","author","languages"))
#
#     context = {
#         "test_form_factory": test_form_factory
#     }
#
#     # context = {
#     #     "current_time": datetime.now(),
#     #     "person": {
#     #         "name": "**<i>Ivan</i>**",
#     #         "age": 20
#     #     },
#     #     "ids": ["list_position1", "list_position2", "list_position3"],
#     #     "some_text": "Hello there",
#     #     "users": [
#     #         "pesho",
#     #         "ivan",
#     #         "stamat",
#     #         "saria",
#     #         "magdalena"
#     #     ]
#     # }
#
#     # form = PersonForm(request.POST or None)
#     #
#     # if request.method == "post":
#     #     print(request.POST['person_name'])
#     #
#     # if form.is_valid():
#     #     print(form.cleaned_data['person_name'])
#     #
#
#     return render(request, "common/index.html", context)

class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    paginate_by = 2
    success_url = reverse_lazy('dashboard')
    model = Post

    def get_queryset(self):
        queryset = self.model.objects.all()

        if not self.request.user.has_perm('posts.can_approve_posts'):
            queryset = queryset.filter(approved=True)

        if 'query' in self.request.GET:
            query = self.request.GET['query']
            queryset = queryset.filter(title__icontains=query)

        return queryset


# # function view
# def dashboard(request):
#     form = SearchForm(request.GET)
#     posts = Post.objects.all()
#
#     if request.method == "GET":
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             posts = posts.filter(title__icontains=query)
#
#     context = {
#         "posts": posts,
#         "form": form,
#     }
#
#     return render(request, 'posts/dashboard.html', context)


def approve_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.approved = True
    post.save()

    return redirect(request.META.get('HTTP_REFERER'))


class AddPostView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    model = Post
    template_name = "posts/add-post.html"
    success_url = reverse_lazy('dashboard')

# # function view
# def add_post(request):
#     form = PostCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard")
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, "posts/add-post.html", context)


class EditPostView(UpdateView):
    model = Post
    template_name = "posts/edit-post.html"
    fields = '__all__'
    success_url = reverse_lazy('dashboard')


# # function view
# def edit_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#
#     if request.method == "POST":
#         form = PostEditForm(request.POST,instance=post)
#
#         if form.is_valid():
#             # # my try
#             # post.title= form.cleaned_data['title']
#             # post.content = form.cleaned_data['content']
#             # post.author = form.cleaned_data['author']
#             # post.languages = form.cleaned_data['languages']
#
#             # # my try 2
#             # for post_field, cleaned_value in form.cleaned_data.items():
#             #     setattr(post, post_field, cleaned_value)
#
#             post.save()
#             return redirect("dashboard")
#     else:
#         form = PostEditForm(instance=post)
#     context = {
#         'form': form,
#         'post': post,
#     }
#
#     return render(request, "posts/edit-post.html", context)

class DeletePostView(DeleteView, FormView):
    model = Post
    form_class = PostDeleteForm
    template_name = "posts/delete-post.html"
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        # another detailed way
        # pk = self.kwargs.get(self.pk_url_kwarg)
        # post = Post.objects.get(pk=pk)
        # return post.__dict__
        return self.get_object().__dict__


# # function view
# def delete_post(request, pk: int):
#     post = Post.objects.get(pk=pk)
#     form = PostDeleteForm(instance=post)
#
#     if request.method == "POST":
#         post.delete()
#         return redirect("dashboard")
#
#     context = {
#         'form': form,
#         'post': post,
#     }
#
#     return render(request, "posts/delete-post.html", context)

class DetailsPostView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect("details-post", pk=post.id)

        # context = self.get_context_data()
        # context['formset'] = formset
        #
        # return self.render_to_response(context)


# # function view
# def details_post(request, pk:int):
#     post = Post.objects.get(pk=pk)
#     formset = CommentFormSet(request.POST or None)
#
#     if request.method == "POST":
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data:
#                     comment = form.save(commit=False)
#                     comment.post = post
#                     comment.save()
#
#             return redirect("details-post", pk=post.id)
#
#     context = {
#         'post': post,
#         'formset': formset,
#     }
#
#     return render(request, "posts/details-post.html", context)


class RedirectHomeView(RedirectView):
    url = reverse_lazy('index') # static

    # def get_redirect_url(self, *args, **kwargs): #dynamic
    #     pass
