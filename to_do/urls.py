from django.urls import path
from .views import HomePageView, ToDoDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', ToDoDetailsView.as_view(), name='to_do_details'),
]