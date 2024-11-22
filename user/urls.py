from django.urls import path
from user.views import *


urlpatterns = [
    path ('', Login, name="Login"),
    path ('cadastro', Cadastro,  name="cadastro"),
    path ('perfil', Perfil, name="perfil"),
]