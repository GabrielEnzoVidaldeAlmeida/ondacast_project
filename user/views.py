from django.shortcuts import render

def Login(request):
    return render(request, "user/login.html")

def Cadastro(request):
    return render(request, "user/cadastro.html")

def Index(request):
    return render(request, "user/index.html")

def inicial_deslogado(request):
    return render(request, "user/inicial_deslogado.html")