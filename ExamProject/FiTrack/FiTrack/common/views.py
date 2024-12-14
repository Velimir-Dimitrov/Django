from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class HomePage(TemplateView):
    template_name = 'common/project.html'

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']
        else:
            return ['common/index_logged_out.html']