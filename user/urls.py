from django.urls import path
from user.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ('login/', Login, name="Login"),
    path ('cadastro/', Cadastro,  name="cadastrar"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path ('perfil', Perfil, name="perfil"),
    path ('configuracoes', Configuracoes, name="configuracoes"),
    path ('login_criador', Login_Criador, name="login_criador"),
    path ('cadastro_criador', Cadastro_Criador, name="cadastro_criador"),
]