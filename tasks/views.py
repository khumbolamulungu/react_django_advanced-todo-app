from django.shortcuts import render
from .models import Task
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):

    model = Task

    template_name = 'tasks/index.html'

    context_object_name = 'all_todos'


class TodoEditView(UpdateView):

    model = Task

    template_name = 'tasks/edit.html'

    fields = ['task', 'description']



class TodoCreateView(CreateView):

    model = Task

    template_name = 'tasks/create.html'

    fields = ['task', 'description']



class TodoDeleteView(DeleteView):

    model = Task

    template_name = 'tasks/delete.html'

    context_object_name = 'todo'

    success_url = reverse_lazy('home')