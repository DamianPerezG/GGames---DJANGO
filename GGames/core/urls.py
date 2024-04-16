from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, login, Signup, Modify, pago, forgot_password, Accion, Carreras, FreeToPlay, MundoAbierto, Supervivencia, Terror

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('Signup/', Signup, name="Signup"),
    path('Modify/', Modify, name="Modify"),
    path('pago/', pago, name="pago"),
    path('login/forgot_password/', forgot_password, name="forgot_password"),
    path('Accion/', Accion, name="Accion"),
    path('Carreras/', Carreras, name="Carreras"),
    path('FreeToPlay/', FreeToPlay, name="FreeToPlay"),
    path('Mundoabierto/', MundoAbierto, name="MundoAbierto"),
    path('Supervivencia/', Supervivencia, name="Supervivencia"),
    path('Terror/', Terror, name="Terror")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
