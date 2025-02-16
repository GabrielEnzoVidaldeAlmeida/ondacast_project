from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from podcast.models import Podcast  # Certifique-se de que este import está correto

class Command(BaseCommand):  # O nome da classe deve ser exatamente "Command"
    help = "Cria os grupos 'Usuário' e 'Criador' com permissões apropriadas"

    def handle(self, *args, **kwargs):
        # Criando ou obtendo os grupos
        grupo_usuario, _ = Group.objects.get_or_create(name="Usuário")
        grupo_criador, _ = Group.objects.get_or_create(name="Criador")

        # Definindo permissões para Criador
        tipo_conteudo = ContentType.objects.get_for_model(Podcast)
        permissoes = Permission.objects.filter(content_type=tipo_conteudo)

        grupo_criador.permissions.set(permissoes)  # Criador tem todas as permissões sobre Podcast

        self.stdout.write(self.style.SUCCESS("Grupos criados ou já existentes!"))
