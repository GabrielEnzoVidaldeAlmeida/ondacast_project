from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError 


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
            usuario.groups.add(Group.objects.get(name="Usuário"))
            usuario.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")  
        except:
            messages.error(request, "Erro ao criar usuário. Tente novamente.")
            return redirect("cadastro")
  
    return render(request, "user/cadastro.html")

def login_criador(request):
    if request.method == "POST":
        nome_podcast = request.POST["nome_podcast"]
        senha = request.POST["password"]
        usuario = authenticate(request, username=nome_podcast, password=senha)
        
        if usuario is not None:
            login(request, usuario)
            return redirect("index_criador")
        else:
            messages.error(request, "nome de usuário ou senha incorretos.")
        
    return render(request, "user/login_criador.html")
        

def cadastro_criador(request):
    print('cadastro_criador')  # Depuração

    if request.method == "POST":
        print('POST recebido')  # ✅ Adicionei um print para debug

        nome_podcast = request.POST["nome_podcast"]
        email = request.POST["email"]
        senha = request.POST["password1"]
        senha_confirmada = request.POST["password2"]

        if senha != senha_confirmada:
            messages.error(request, "As senhas não coincidem.")
            return redirect("cadastro_criador")

        try:
            usuario = User.objects.create_user(username=nome_podcast, email=email, password=senha)
            
            try:
                grupo = Group.objects.get(name="Criador") 
            except Group.DoesNotExist:  
                messages.error(request, "Erro: Grupo 'Criador' não existe. Contate um administrador.")
                return redirect("cadastro_criador")

            usuario.groups.add(grupo)
            messages.success(request, "Podcast cadastrado com sucesso!")
            return redirect("login_criador")  
        
        except IntegrityError:
            messages.error(request, "Nome do podcast ou e-mail já está em uso. Escolha outro.")
            return redirect("cadastro_criador")

    return render(request, "user/cadastro_criador.html")
   

@login_required
def excluir_conta(request):
    usuario = request.user  # Obtém o usuário autenticado
    
    
    # Impede a exclusão de superusuários
    if usuario.is_superuser:
        messages.error(request, "Superusuários não podem excluir suas contas.")
        return redirect("configuracoes")  

    if request.method == "POST":
        usuario.delete()  # Exclui o usuário do banco de dados
        logout(request)  
        messages.success(request, "Sua conta foi excluída com sucesso!")
        return redirect("login") 
    
    return redirect("configuracoes")  
def sair_criado(request):
    logout(request)
    return redirect("login_criador")
    
def sair(request):
    logout(request)
    return redirect("login")


def inicial_deslogado(request):
    return render(request, "user/inicial_deslogado.html")

def Perfil(request):
    return render(request, "user/perfil.html")

def Configuracoes(request):
    return render(request, "user/configuracoes.html")



