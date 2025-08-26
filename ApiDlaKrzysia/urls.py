from django.urls import path
from .views import ListaZadanCreate, ListaZadanDetail, ListaZadanStatus

urlpatterns = [
    path('api/', ListaZadanCreate.as_view(), name='todo-list-create'),
    path('api/<int:pk>/', ListaZadanDetail.as_view(), name='todo-detail'),
    path('api/<int:pk>/status/', ListaZadanStatus.as_view(), name='todo-detail'),
]

# pozbyc sie iscomplited
# uuid you fucking idiot , endpoint
    # 'potezneapi/<int:pk>/status/ put status poslany
    # lista userow, opcja zalogowania sie, zarejestrowania, zmiany hasla, resetu hasla kod z fajkowego maila,
    # setupowanie po mailu jest trudne Dla Krzycha
    # 2 endpointy... 1 generuje klucz...2 przyjmuje nowe haslo i klucz.
    # token sesji, duuuzo sprawdzania , kurwa za chuja mi sie nie chce sprawdzac, libka z django, autentication system,
    # oooo poczekaaaaaj, on moze zarzadzac kontami wooow, no musisz sobie oddac jeden modul w django,
    # leee to jednak japierdole https://docs.djangoproject.com/en/5.2/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware