from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

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
