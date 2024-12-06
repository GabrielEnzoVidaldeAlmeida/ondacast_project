from django.urls import path
from podcast.views import *

urlpatterns = [
    path ('index', Index, name='index'),
    path ('', InicialDeslogado, name="inicial_deslogado"),
]
