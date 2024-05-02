from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, login, Signup, Modify, pago, forgot_password, Accion, Carreras, FreeToPlay, MundoAbierto, Supervivencia, Terror, create
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name='core/Login.html'), name='login'),
    path('forgot_password/', forgot_password, name="forgot_password"),    
    path('Signup/', Signup, name="Signup"),
    path('Modify/', Modify, name="Modify"),
    path('pago/', pago, name="pago"),
    path('Accion/', Accion, name="Accion"),
    path('Carreras/', Carreras, name="Carreras"),
    path('FreeToPlay/', FreeToPlay, name="FreeToPlay"),
    path('Mundoabierto/', MundoAbierto, name="MundoAbierto"),
    path('Supervivencia/', Supervivencia, name="Supervivencia"),
    path('Terror/', Terror, name="Terror"),
    path('read/', views.read, name= "Inventario"),
    path('create/', views.create, name= "IngresoInventario"),
    path('update/', views.create, name= "UpdateInventario"),
    path('update/', views.create, name= "DeleteInventario"),
    path('carrito/', views.create, name= "CarritoCompra"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
