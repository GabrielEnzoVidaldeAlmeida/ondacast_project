from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def entrar(request):
    if request.method == "POST":
        nome_usuario = request.POST["username"]
        senha = request.POST["password"]
        usuario = authenticate(request, username=nome_usuario, password=senha)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("index")
        else:
            messages.error(request, "nome de usuário ou senha incorretos.")
        
    return render(request, "user/login.html")

def cadastrar(request):
    if request.method == "POST":
        nome_usuario = request.POST["username"]
        email = request.POST["email"]
        senha = request.POST["password"]
        senha_confirmada = request.POST["password2"]

        if senha != senha_confirmada:
            messages.error(request, "As senhas não coincidem.")
            return redirect("cadastro")

        # Criar o novo usuário
        try:
            usuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")  
        except:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            return redirect("cadastro")

    return render(request, "user/cadastro.html")


@login_required
def excluir_conta(request):
    usuario = request.user  # Obtém o usuário autenticado
    
    # Impede a exclusão de superusuários
    if usuario.is_superuser:
        messages.error(request, "Superusuários não podem excluir suas contas.")
        return redirect("configuracoes")  

    if request.method == "POST":
        usuario.delete()  # Exclui o usuário do banco de dados
        logout(request)  # Faz logout automaticamente
        messages.success(request, "Sua conta foi excluída com sucesso!")
        return redirect("login")  # Redireciona para a página de login
    
    return redirect("configuracoes")  # Se não for POST, apenas recarrega a página
    
def sair(request):
    logout(request)
    return redirect("login")


def inicial_deslogado(request):
    return render(request, "user/inicial_deslogado.html")

def Perfil(request):
    return render(request, "user/perfil")

def Configuracoes(request):
    return render(request, "user/configuracoes.html")

def Login_Criador(request):
    return render(request, "user/login_criador.html")

def Cadastro_Criador(request):
    return render(request, "user/cadastro_criador.html")