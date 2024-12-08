from django.urls import path
from podcast.views import *

urlpatterns = [
    path ('index', Index, name='index'),
    path ('podcast', podcastPage, name='podcast_page'),
    path ('', InicialDeslogado, name="inicial_deslogado"),
    path ('index_criador', indexCriador, name='index_criador'),
]
