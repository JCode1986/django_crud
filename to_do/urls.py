from django.urls import path
from .views import HomePageView, ToDoDetailsView, ToDoDeleteView, ToDoCreateView, ToDoUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', ToDoDetailsView.as_view(), name='to_do_details'),
    path('to_do/delete/', ToDoDeleteView.as_view(), name='to_do_delete'),
    path('to_do/create/', ToDoCreateView.as_view(), name='to_do_create'),
    path('to_do/update/', ToDoUpdateView.as_view(), name='to_do_update'),
]