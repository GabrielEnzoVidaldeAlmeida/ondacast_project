from django.urls import path
from podcast.views import *

urlpatterns = [
    path ('index', Index, name='index'),
<<<<<<< HEAD
    path ('deslogado', InicialDeslogado, name="inicial_deslogado"),
    path ('podcast', podcastPage, name="podcast_page"),
=======
    path ('', InicialDeslogado, name="inicial_deslogado"),
>>>>>>> origin/develop
]
