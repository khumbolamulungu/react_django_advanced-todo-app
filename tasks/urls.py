from django.urls import path
from .views import HomeView, TodoEditView, TodoCreateView, TodoDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('edit/<int:pk>/', TodoEditView.as_view(), name='edit'),
    path('create/', TodoCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
]