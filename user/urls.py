from django.urls import path
from user.views import Login

urlpatterns = [
    path ('', Login, name="Login"),
]