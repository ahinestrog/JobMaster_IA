from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.contrib.auth import authenticate, login, logout
from .models import CV
from .forms import CreateUserForm, CVForm, CVInfoForm
from django.contrib import messages
import os
import openai
from dotenv import load_dotenv
import pypandoc

# Create your views here.

def get_completion(prompt, model="gpt-3.5-turbo"):
    # Obtiene la clave API de las variables de entorno
    api_key = os.getenv('openai_apikey')
    
    openai.api_key = api_key
    
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def create_file(form):
    prompt = f"Crea un texto en formato markdown lo mas detallado posible que contenga una hoja de vida para un trabajo con el título {form.cleaned_data['jobTitle']}, la hoja de vida debe estar orientada a esta descripcion: {form.cleaned_data['description']}, la vacante tiene estos {form.cleaned_data['requirements']} , la hoja de vida debe ser muy detallada y debe contener: Mi nombre: {form.cleaned_data['fullName']},  mi correo {form.cleaned_data['email']} y esta experiencia que tengo en los requisitos para el trabajo {form.cleaned_data['experienceYears']}"
    response = get_completion(prompt)

    with open('CVGenerator/media/CV/files/CV.md', 'w') as file:
        file.write(response)
        
    try:
        pypandoc.convert_file('CVGenerator/media/CV/files/CV.md', 'docx', outputfile='CVGenerator/media/CV/files/CV.docx')
    except:
        print('Error al convertir el archivo')

def download_docx(request):
    docx_file = 'CVGenerator/media/CV/files/CV.docx'

    # Verificar si el archivo existe
    if os.path.exists(docx_file):
        # Devuelve el archivo
        response = FileResponse(open(docx_file, 'rb'))
        return response
    else:
        # Si no existe, devuelve un error 404
        raise Http404("El archivo solicitado no existe")

def home(request):
    query = request.GET.get('query', '')

    all_jobs = [
        {'title': 'Desarrollador Web', 'company': 'Empresa A', 'location': 'Medellín'},
        {'title': 'Diseñador Gráfico', 'company': 'Empresa B', 'location': 'Bogotá'},
    ]

    if query:
        jobs = [job for job in all_jobs if query.lower() in job['title'].lower()]
    else:
        jobs = all_jobs

    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'home.html', {'jobs': jobs})

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


def desarrollador_full_stack(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'desarrollador_full_stack.html')

def administrador_proyectos(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'administrador_proyectos.html')

def abogado_corporativo(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'abogado_corporativo.html')

def limpiador_profesional(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'limpiador_profesional.html')

def desarrollador_backend(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'desarrollador_backend.html')

def asistente_administrativo(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'asistente_administrativo.html')

def gerente_proyectos(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'gerente_proyectos.html')

def contador_publico(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'contador_publico.html')

def ingeniero_devops(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'ingeniero_devops.html')

def recepcionista(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'recepcionista.html')

def diseno_grafico(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'diseno_grafico.html')

def analista_datos(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'analista_datos.html')

def analista_recursos_humanos(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'analista_recursos_humanos.html')

def ingeniero_soporte_tecnico(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'ingeniero_soporte_tecnico.html')

def auxiliar_almacen(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'auxiliar_almacen.html')

def diseno_ux_ui(request):
    if request.method == 'POST':
        form = CVInfoForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
        else:
            print(form.errors)
    return render(request, 'diseno_ux_ui.html')