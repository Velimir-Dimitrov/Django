from django.urls import reverse_lazy
from django.views.generic import CreateView
from forumApp.accounts.forms import CustomUserForm


# Create your views here.


class UserRegister(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')