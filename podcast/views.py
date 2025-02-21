from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Episodio, Podcast
from .forms import EpisodioForm, EditarPodcastForm, ExcluirEpisodioForm



@login_required
def Index(request):
    return render(request, "podcast/index.html")

def InicialDeslogado(request):
    return render(request, "podcast/inicial_deslogado.html")
@login_required
def podcastPage(request):
    return render(request, "podcast/podcast_page.html")
@login_required
def index_Criador(request):
    podcast = Podcast.objects.filter(usuario=request.user).first()
    return render(request, "podcast/index_criador.html",{'podcast':podcast})
@login_required
def Favoritos(request):
    return render(request, "podcast/favoritos.html")
@login_required
def Downloads(request):
    return render(request, "podcast/downloads.html")

@login_required
def AdicionarEpisodio(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        capa = request.FILES.get("capa")
        arquivo_audio = request.FILES.get("arquivo_audio")

        if not titulo or not descricao or not capa or not arquivo_audio:
            messages.error(request, "Por favor, preencha todos os campos!")
            return render(request, 'podcast/adicionar_episodio.html')


        Episodio.objects.instance(
            podcast=request.user,
            titulo=titulo,
            descricao=descricao,
            capa=capa,
            arquivo_audio=arquivo_audio,
        )

        messages.success(request, "Episódio adicionado com sucesso!")

    return render(request, 'podcast/adicionar_episodio.html')


@login_required

def EstatisticasCriador(request):
    return render(request, "podcast/estatisticas_criador.html")

@login_required
def EditarPerfilCriador(request):
    podcast = get_object_or_404(Podcast, usuario=request.user)

    if request.method == 'POST':
        form = EditarPodcastForm(request.POST, request.FILES, instance=podcast)
        if form.is_valid():
            form.save()
            return redirect('index_criador',podcast_id=podcast.id)
    else:
        form = EditarPodcastForm(instance=podcast)

    return render(request, "podcast/editar_perfil_criador.html", {'form': form, 'podcast': podcast})


@login_required
def ExcluirEpisodio(request):
    return render(request, "podcast/editar_perfil_criador.html")