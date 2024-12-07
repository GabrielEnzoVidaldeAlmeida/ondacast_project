from django.shortcuts import render

def Index(request):
    return render(request, "podcast/index.html")

def InicialDeslogado(request):
    return render(request, "podcast/inicial_deslogado.html")

def podcastPage(request):
    return render(request, "podcast/podcast_page.html")