from django.urls import path
from podcast.views import *

urlpatterns = [
    path ('OndaCast', Index, name='index'),
    path ('', InicialDeslogado, name="inicial_deslogado"),
]
