from django.urls import path
from podcast.views import *

urlpatterns = [
    path ('index', Index, name='index'),
    path ('podcast', podcastPage, name='podcast_page'),
    path ('', InicialDeslogado, name="inicial_deslogado"),
    path ('index_criador', indexCriador, name='index_criador'),
    path ('favoritos', Favoritos, name='favoritos'),
    path ('downloads', Downloads, name='downloads'),
    path ('adicionar_episodio', AdicionarEpisodio, name='adicionar_episodio'),
    path ('estatisticas_criador', EstatisticasCriador, name='estatisticas_criador'),
]
