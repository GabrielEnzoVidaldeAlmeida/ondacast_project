from django.urls import path
from user.views import *


urlpatterns = [
    path ('login', Login, name="Login"),
    path ('cadastro', Cadastro,  name="cadastro"),
    path ('perfil', Perfil, name="perfil"),
    path ('configuracoes', Configuracoes, name="configuracoes"),
    path ('login_criador', Login_Criador, name="login_criador"),
    path ('cadastro_criador', Cadastro_Criador, name="cadastro_criador"),
]