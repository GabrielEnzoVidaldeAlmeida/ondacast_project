from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path ('index', Index, name='index'),
    path ('podcast', podcastPage, name='podcast_page'),
    path ('', InicialDeslogado, name="inicial_deslogado"),
    path ('index_criador', views.index_criador, name='index_criador'),
    path ('favoritos', Favoritos, name='favoritos'),
    path ('downloads', Downloads, name='downloads'),
    path ('adicionar_episodio', views.AdicionarEpisodio,name='adicionar_episodio'),
    path ('estatisticas_criador', EstatisticasCriador, name='estatisticas_criador'),
    path ('editar_perfil_criador', EditarPerfilCriador, name='editar_perfil_criador'),
]
