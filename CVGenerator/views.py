from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CV
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)

            return redirect('http://127.0.0.1:8000/login/')

    context = {'form': form}
    return render(request,'register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        
        else:
            messages.info(request,'Username OR password is incorrect')
        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/login/')