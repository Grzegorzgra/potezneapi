from django.urls import path
from .views import ListaZadanCreate, ListaZadanDelete

urlpatterns = [
    path('potezneapi/', ListaZadanCreate.as_view(), name='todo-create'),
    path('potezneapi/<int:pk>/', ListaZadanDelete.as_view(), name='todo-delete'),
]