from django.shortcuts import render

def Login(request):
    return render(request, "user/login.html")

def Cadastro(request):
    return render(request, "user/cadastro.html")

def inicial_deslogado(request):
    return render(request, "user/inicial_deslogado.html")

def Perfil(request):
    return render(request, "user/perfil.html")

def Configuracoes(request):
    return render(request, "user/configuracoes.html")

def Login_Criador(request):
    return render(request, "user/login_criador.html")

def Cadastro_Criador(request):
    return render(request, "user/cadastro_criador.html")