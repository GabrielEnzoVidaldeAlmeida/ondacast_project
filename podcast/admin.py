from django.contrib import admin
from .models import Podcast, Episodio

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ("nome", "usuario", "data_criacao")
    search_fields = ("nome", "usuario__username")
    list_filter = ("data_criacao",)
    ordering = ("-data_criacao",)
    readonly_fields = ("data_criacao",)

@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "podcast", "get_data_publicacao")
    search_fields = ("titulo", "podcast__nome")
    list_filter = ("podcast",)
    ordering = ("-data_publicacao",)
    readonly_fields = ("data_publicacao",)

    def get_data_publicacao(self, obj):
        return obj.data_publicacao.strftime("%d/%m/%Y %H:%M")
    
    get_data_publicacao.short_description = "Data de Publicação"
    get_data_publicacao.admin_order_field = "data_publicacao"  # Permite ordenação
