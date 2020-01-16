from django.urls import path
from .views import HomePageView, ToDoDetailsView, BlogDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', ToDoDetailsView.as_view(), name='to_do_details'),
    path('delete/', BlogDeleteView.as_view(), name='to_do_delete'),
]