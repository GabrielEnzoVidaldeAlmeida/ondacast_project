from django.shortcuts import render

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
    return render(request, "podcast/adicionar_episodio.html")