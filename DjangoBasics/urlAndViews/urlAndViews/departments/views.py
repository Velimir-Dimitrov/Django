import json
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from urlAndViews.asgi import application
from urlAndViews.departments.models import Department


# Create your views here.

def index(request):
    url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f"<h1>{url} {url_lazy}</h1>")

def view_with_variable(request, variable):
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request,"departments/name_template.html", {'variable':variable}, status=302)

def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")

def view_with_int_pk(request, pk):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>", content_type="text/plain") #text example
    # return HttpResponse(json.dumps({"pk": pk}), content_type="application/json")
    # return JsonResponse({"pk": pk})   # option 2 makes same thing with abstraction

def view_with_slug(request, pk, slug):

    # Option 1 for 404:
    # department = Department.objects.filter(pk=pk, slug=slug).first()
    #
    # if not department:
    #     raise Http404 # option for custom webpage in templated for debug off in settings

    # Option 2
    # return HttpResponseNotFound()

    # Option 3
    # return HttpResponse(404)

    # Option 4
    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")

def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect("https://softuni.bg/")

def redirect_to_view(request):
    # return redirect("http://localhost:8000") #breaks abstraction- can be used only for redirect to other projects/websites
    # return redirect(index) #breaks single responsibility if we use another app
    return redirect('numbers', pk=2) # best option