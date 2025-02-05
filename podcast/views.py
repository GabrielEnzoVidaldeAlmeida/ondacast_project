from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Episodio, Podcast
from .forms import EpisodioForm, EditarPodcastForm, ExcluirEpisodioForm

@login_required

def Index(request):
    return render(request, "podcast/index.html")

def InicialDeslogado(request):
    return render(request, "podcast/inicial_deslogado.html")

def podcastPage(request):
    return render(request, "podcast/podcast_page.html")

def indexCriador(request):
    return render(request, "podcast/index_criador.html")

def Favoritos(request):
    return render(request, "podcast/favoritos.html")

def Downloads(request):
    return render(request, "podcast/downloads.html")

def AdicionarEpisodio(request):
    if request.method == 'POST':
        form = EpisodioForm(request.POST, request.FILES)
        if form.is_valid():
            episodio = form.save(commit=False)
            episodio.criador = request.user
            episodio.save()
            return redirect('index_criador')
    else:
        form = EpisodioForm()
        
    return render(request, "podcast/adicionar_episodio.html", {'form': form})

def EstatisticasCriador(request):
    return render(request, "podcast/estatisticas_criador.html")

def EditarPerfilCriador(request):
    podcast = get_object_or_404(Podcast, id= podcast_id, criador=request.user)

    if request.method == 'POST':
        form = EditarPodcastForm(request.POST, request.FILES, instance=podcast)
        if form.is_valid():
            form.save()
            return redirect('index_criador',podcast_id=podcast.id)
    else:
        form = EditarPodcastForm(instance=podcast)

    return render(request, "podcast/editar_perfil_criador.html", {'form': form, 'podcast': podcast})

def ExcluirEpisodio(request):
    episodio = get_object_or_404(Episodio, id=episodio_id, criador=request.user)

    if request.method == 'POST':
        form = ExcluirEpisodioForm(request.POST, instance=episodio)
        if form.is_valid():
            episodio.delete()
            return redirect('index_criador', podcast_id=episodio.podcast.id)
    else:
        form = ExcluirEpisodioForm(instance=episodio)

    return render(request, "podcast/excluir_episodio.html", {'form': form, 'episodio': episodio})