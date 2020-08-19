from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
from .forms import UserCreateForm


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
