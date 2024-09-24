from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CV
from .forms import CreateUserForm, CVForm
from django.contrib import messages
import os
from openai import OpenAI
from dotenv import load_dotenv

# Create your views here.

def get_completion(prompt, model="gpt-3.5-turbo"):
    _ = load_dotenv('api_keys.env')
    client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('api_key_3_2'),
    )
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

def create_file(form):
    prompt = f"Crea un texto en formato markdown lo mas detallado posible que contenga una hoja de vida para conseguir un trabajo muy importante, que sea muy detallada y que contenga lo siguiente: Mi nombre: {form.cleaned_data['name']}, {form.cleaned_data['prompt']}, {form.cleaned_data['education']}, estos idiomas que hablo {form.cleaned_data['languages']}, esta experiencia que tengo {form.cleaned_data['experience']}, con este telefono {form.cleaned_data['phone']} y este correo {form.cleaned_data['email']}"
    response = get_completion(prompt)

    with open('CVGenerator/media/CV/files/CV.md', 'w') as file:
        file.write(response)


def home(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
            #return redirect('http://127.0.0.1:8000/dispFile/')
        else:
            print(form.errors)
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