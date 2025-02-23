from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Episodio(models.Model):
    episodio_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='podcast/media/capas')
    arquivo_audio = models.FileField(upload_to='podcast/media/episodios')
    podcast = models.ForeignKey('Podcast', on_delete=models.CASCADE, default=1)
    data_publicacao = models.DateTimeField(default=timezone.now)  # Campo de data

    def __str__(self):
        return self.titulo

class Podcast(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='media/fotos', default='media/fotos/img/user-default.jpg')
    data_criacao = models.DateTimeField(default=timezone.now)  # Campo de data

    def __str__(self):
        return self.nome

