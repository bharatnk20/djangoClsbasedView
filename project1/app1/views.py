from django.http import HttpResponse
from django.shortcuts import render,reverse

from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView, FormView
# Create your views here.

from . models import FinnModel
from . forms import FinnForm

from django.core.exceptions import *


def home(request):
    return render(request,'app1/home.html')


class MyView(View):
    def get(self,request):
        return HttpResponse('<h1>About Us Page</h1>')


class FinnCreate(CreateView):
    #specify the model for CreateView

    model = FinnModel
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('home',)


class FinnList(ListView):
    model = FinnModel


class FinnDetail(DetailView):
    model = FinnModel



class FinnUpdate(UpdateView):
    model = FinnModel
    fields = "__all__"

    # def get_success_url(self):
    #     return reverse('home',)
    success_url = '/'


class FinnDelete(DeleteView):
    model = FinnModel

    success_url = '/'


class FinnFormContact(FormView):
    form_class = FinnForm

    template_name = 'app1/FinnModel_form.html'

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/thanks/"