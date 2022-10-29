from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from AppCoder.models import Curso
from crispy_forms.utils import render_crispy_form

def inicio(request):
    return render(request, "inicio.html")

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre':'Derick','apellido':'Carcamo', 'lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

#def cursos(self):
#    #planilla = loader.get_template('cursos.html')
#    curso = Curso(nombre="UX/UI", camada="12345")
#    curso.save()
#    
#    documento = f'Curso: {curso.nombre} camada: {curso.camada}' 
#    return HttpResponse(documento)