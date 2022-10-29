from re import template
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name="Logout" ),
    path('home/pages/', home),
    path('home/pages/blog/', blog),
    path('perfil/', perfilView),
    path('regitrarblog/', Registrarblog),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/changepass/', changepass),
    path('perfil/changeAvatar/', AgregarAvatar)
]