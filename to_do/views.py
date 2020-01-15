from django.views.generic import ListView, DetailView
from .models import Post

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'

class ToDoDetailsView(DetailView):
    template_name = 'to_do_details.html'
    model = Post
