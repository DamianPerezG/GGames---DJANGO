from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):  # Cambia el nombre de la vista aquí
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pswd')
        
        # Autenticar al usuario con las credenciales proporcionadas
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Si las credenciales son válidas, iniciar sesión para el usuario
            login(request, user)
            return redirect('/')  # Redirigir a la página principal o a donde sea necesario después del inicio de sesión
        else:
            # Si las credenciales son inválidas, mostrar un mensaje de error
            context = {'error_message': 'Credenciales inválidas. Verifica tu email y contraseña.'}
            return render(request, 'core/login.html', context)

    return render(request, 'core/login.html')
        
def Signup(request):
    return render(request,'core/Signup.html')

def Modify(request):
    return render(request,'core/Modify.html')

def pago(request):
    return render(request,'core/pago.html')

def forgot_password(request):
    return render(request,'core/forgot_password.html')

def Accion(request):
    return render(request,'core/Accion.html')

def Carreras(request):
    return render(request,'core/Carreras.html')

def FreeToPlay(request):
    return render(request,'core/FreeToPlay.html')

def MundoAbierto(request):
    return render(request,'core/MundoAbierto.html')

def Supervivencia(request):
    return render(request,'core/Supervivencia.html')

def Terror(request):
    return render(request,'core/Terror.html')

def create(request):
    return render(request,'core/create.html')

def read(request):
    return render(request,'core/read.html')

def update(request):
    return render(request,'core/update.html')

def delete(request):
    return render(request,'core/delete.html')

def carrito(request):
    return render(request,'core/carrito.html')
