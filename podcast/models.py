from django.db import models
from django.contrib.auth.models import User


class Episodio(models.Model):
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='podcast/media/capas')
    arquivo_audio = models.FileField(upload_to='podcast/media/episodios')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo