from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Blogs, IMGBlogs, IMGUser
from AppCoder.forms import form_registraBlog, UserRegisterForm, UserEditForm, ChangePasswordForm, AvatarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    avatar = IMGUser.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None

    blogs = Blogs.objects.all()
    if(blogs != None):
        print(blogs[0].imagenBlog.imagen.url)
        return render(request, 'home.html', {'avatar':avatar,'blogs':blogs})
    else:
        return render(request, 'home.html', {'avatar':avatar,'msg':'no hay blogs que mostrar'})

@login_required
def blog(request):
    print(request.GET.get('id'))
    blogs = Blogs.objects.get(id=request.GET.get('id'))
    return render(request, 'blog.html',{'blogs':blogs})

@login_required
def Registrarblog(request):
    if request.method == "POST":
        formulario = form_registraBlog(request.POST,  request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            print(informacion)
            user = User.objects.get(username = request.user)
            imagenblog2 = IMGBlogs(imagen = informacion['imagenBlog'])
            imagenblog2.save()
            blog = Blogs(autor = user, titulo = informacion['titulo'],subtitulo = informacion['subtitulo'], blogCompleto = informacion['blogCompleto'])
            blog.imagenBlog = imagenblog2
            blog.save()
            
            avatar = IMGUser.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            #return render(request, 'home.html', {'avatar': avatar})
            blogs = Blogs.objects.all()
            if(blogs != None):
                print(blogs[0].imagenBlog.imagen.url)
                return render(request, 'home.html', {'avatar':avatar,'blogs':blogs})
            else:
                return render(request, 'home.html', {'avatar':avatar,'msg':'no hay blogs que mostrar'})
    else:
        avatar = IMGUser.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None           
        formulario = form_registraBlog()
    return render(request, "registraBlog.html", {"formulario": formulario})


def login_request(request):
    form = AuthenticationForm(request, data = request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)
            print(user)
            if user is not None:
                login(request, user)
                avatar = IMGUser.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None

                print(Blogs.objects.all().values())
                blogs = Blogs.objects.all()
                if(blogs != None):
                    print(blogs[0].imagenBlog.imagen.url)
                    #return render(request, 'home.html', {'avatar':avatar,'blogs':blogs})
                    return redirect("/interno/home/pages/")
                else:
                    #return render(request, 'home.html', {'avatar':avatar,'msg':'no hay blogs que mostrar'})
                    return redirect("/interno/home/pages/")
                
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    form = UserRegisterForm(request.POST)
    print(request.method)
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)       
        #print(form)# debugeee
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            return redirect("/interno/login")
        else:#decidi regresar el formulario con error
            return render(request, "registro.html", {'form': form})
    #form = UserCreationForm()
    form = UserRegisterForm()
    return render(request, "registro.html", {'form': form})


def about(request):
    #usuario = request.user
    #user_basic_info = User.objects.get(id = usuario.id)
    #return render(request, "about.html", {'firstname': user_basic_info.first_name,'lastname':user_basic_info.last_name})
    return render(request, "about.html")


@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = IMGUser.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html', {'avatar': avatar})
        else:
            avatar = IMGUser.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html', {'form':form, 'avatar': avatar})
    else:
        form = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
    return render(request, 'editarPerfil.html', {'form': form, 'usuario': usuario})

@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        #form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = IMGUser.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html', {'avatar': avatar})
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form': form, 'usuario': usuario})

@login_required
def perfilView(request):
    avatar = IMGUser.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'perfil.html', {'avatar': avatar})
            
@login_required
def AgregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = IMGUser(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = IMGUser.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'home.html', {'avatar': avatar})
    else:
        try:
            avatar = IMGUser.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})


