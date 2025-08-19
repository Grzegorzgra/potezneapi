from django.urls import path
from .views import ListaZadanCreate, ListaZadanDetail

urlpatterns = [
    path('potezneapi/', ListaZadanCreate.as_view(), name='todo-list-create'),
    path('potezneapi/<int:pk>/', ListaZadanDetail.as_view(), name='todo-detail'),
]