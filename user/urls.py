from django.urls import path
from user.views import *


urlpatterns = [
    path ('login', Login, name="Login"),
    path ('cadastro', Cadastro,  name="cadastro"),
]