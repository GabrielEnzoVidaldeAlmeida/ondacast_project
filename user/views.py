from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from .forms import RegistrationForm

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
            return redirect('index')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def Cadastro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
            return redirect('index')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = RegistrationForm()
    return render(request, 'user/cadastro.html', {'form': form})

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