from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='connexion/')
def acceuil(request):
    return render(request, 'acceuil.html',)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        new_user = User(username=username, email=email, password=password)
        new_user.save()
        return redirect('connexion')

    return render(request, 'inscription.html')

def logIn(request):
 if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'acceuil.html')
            else:
                messages.error(request,'Identifiant ou mot de passe incorrect')
                return redirect('connexion')
            
 return render(request, 'connexion.html')

def logOut(request):
    logout(request)
    return redirect('acceuil')
