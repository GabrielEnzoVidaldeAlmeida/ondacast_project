from django.urls import path
from . import views
from .views import *
from user.views import editar_podcast

urlpatterns = [
    path ('index', index, name='index'),
    path ('podcast', podcast_page, name='podcast_page'),
    path ('', InicialDeslogado, name="inicial_deslogado"),
    path ('index_criador', views.index_Criador, name='index_criador'),
    path ('downloads', Downloads, name='downloads'),
    path ('adicionar_episodio', views.AdicionarEpisodio,name='adicionar_episodio'),
    path ('estatisticas_criador', EstatisticasCriador, name='estatisticas_criador'),
    path ('editar_perfil_criador', editar_podcast, name='editar_perfil_criador'),
    path('deletar_episodio/<int:episodio_id>/', views.deletar_episodio, name='deletar_episodio'),
    path('podcast/<int:podcast_id>/', podcast_page, name='podcast_page'),
    path('favoritos/', views.Favoritos, name='favoritos'),

]