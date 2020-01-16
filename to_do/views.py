from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post
from django.urls import reverse_lazy


#Import these to urls.py
#also add these to urlpatterns list; ex: [path('', HomePageView.as_view(), name='home'),]
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'

class ToDoDetailsView(DetailView):
    template_name = 'to_do_details.html'
    model = Post

class ToDoCreateView(CreateView):
    template_name = 'to_do_create.html'
    model = Post
    fields = ['title', 'body', 'author']

class ToDoUpdateView(UpdateView):
    template_name = 'to_do_update.html'
    model = Post
    fields = ['title', 'body']

class ToDoDeleteView(DeleteView):
    model = Post
    template_name = 'to_do_delete.html'
    # Delete View needs to define a success_url to know where to go after the deletion
    # Also, note the use of reverse_lazy which navigates away only after confirmation
    success_url = reverse_lazy('home')
