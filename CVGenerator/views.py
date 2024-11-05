from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.contrib.auth import authenticate, login, logout
from .models import CV
from .forms import CreateUserForm, CVForm
from django.contrib import messages
import os
import openai
from dotenv import load_dotenv
import pypandoc

# Create your views here.

def get_completion(prompt, model="gpt-3.5-turbo"):
    # Obtiene la clave API de las variables de entorno
    api_key = os.getenv('openai_apikey')
    
    # Configura la clave API en el cliente de OpenAI
    openai.api_key = api_key
    
    # Crear la solicitud de chat completions
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def create_file(form):
    prompt = f"Crea un texto en formato markdown lo mas detallado posible que contenga una hoja de vida para conseguir un trabajo muy importante, que sea muy detallada y que contenga lo siguiente: Mi nombre: {form.cleaned_data['name']}, {form.cleaned_data['prompt']}, {form.cleaned_data['education']}, estos idiomas que hablo {form.cleaned_data['languages']}, esta experiencia que tengo {form.cleaned_data['experience']}, con este telefono {form.cleaned_data['phone']} y este correo {form.cleaned_data['email']}"
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
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            create_file(form)
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


def desarrollador_full_stack(request):
    return render(request, 'desarrollador_full_stack.html')

def administrador_proyectos(request):
    return render(request, 'administrador_proyectos.html')

def abogado_corporativo(request):
    return render(request, 'abogado_corporativo.html')

def limpiador_profesional(request):
    return render(request, 'limpiador_profesional.html')

def desarrollador_backend(request):
    return render(request, 'desarrollador_backend.html')

def asistente_administrativo(request):
    return render(request, 'asistente_administrativo.html')

def gerente_proyectos(request):
    return render(request, 'gerente_proyectos.html')

def contador_publico(request):
    return render(request, 'contador_publico.html')

def ingeniero_devops(request):
    return render(request, 'ingeniero_devops.html')

def recepcionista(request):
    return render(request, 'recepcionista.html')

def diseno_grafico(request):
    return render(request, 'diseno_grafico.html')

def analista_datos(request):
    return render(request, 'analista_datos.html')

def analista_recursos_humanos(request):
    return render(request, 'analista_recursos_humanos.html')

def ingeniero_soporte_tecnico(request):
    return render(request, 'ingeniero_soporte_tecnico.html')

def auxiliar_almacen(request):
    return render(request, 'auxiliar_almacen.html')

def diseno_ux_ui(request):
    return render(request, 'diseno_ux_ui.html')