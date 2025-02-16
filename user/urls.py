from django.urls import path
from user.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ('login/',entrar, name="login"),
    path ('cadastro/', cadastrar,  name="cadastro"),
    path('logout/', sair, name="logout"),
    path("excluir_conta", excluir_conta, name="excluir_conta"),
    path ('perfil', Perfil, name="perfil"),
    path ('configuracoes', Configuracoes, name="configuracoes"),
    path ('login_criador', Login_Criador, name="login_criador"),
    path ('cadastro_criador', Cadastro_Criador, name="cadastro_criador"),
]