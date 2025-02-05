from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EpisodioForm

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
    return render(request, "podcast/editar_perfil_criador.html")

