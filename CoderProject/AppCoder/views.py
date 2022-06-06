from django.template import loader 
from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

my_template = loader.get_template('index.html')

def miplantilla(request):
    return render(request, 'AppCoder/inicio.html')
#    plantilla = loader.get_template('inicio.html')
#
#    document = plantilla.render()
#
#    return HttpResponse(document)

#def inicio(self):
#    name = 'jose'
#    last_name = 'aliaga'
#
#    my_list = [2,3,4,5,6,1]
#
#    dictionary = {'nombre':name,'apellido':last_name,'lista':my_list}
#
#    document = my_template.render(dictionary) # ya no necesitamos un contexto
#
#    return HttpResponse(document)

#def cursos(self):
#    course = Curso(name='Desarrollo Web', camada='2989')
#    course.save()
#    document = f'- Curso: {course.name} - camada = {course.camada}'
#
#    return HttpResponse(document)

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse('vista estudiantes')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse('vista entregables')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse('vista cursos')

def formulario(request):
    if request.method == 'POST':
        print(request.POST)
        curso = Curso(name = request.POST['curso'],camada = request.POST['camada'])
        curso.save()
        return render(request,"AppCoder/inicio.html")
    
    return render(request, 'AppCoder/formulario.html')


