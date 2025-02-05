from django.db import models
from django.contrib.auth.models import User


class Episodio(models.Model):
    episodio_id = models.AutoField(primary_key=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='podcast/media/capas')
    arquivo_audio = models.FileField(upload_to='podcast/media/episodios')
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Podcast(models.Model):
    criador = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='podcast/media/fotos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome