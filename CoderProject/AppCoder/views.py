from django.template import loader 
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *

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

class EstudianteFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    submission_date = forms.DateField()
    submitted = forms.BooleanField()

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfeFormulario(request.POST)
        if miFormulario.is_valid(): # parentesisssss

            informacion = miFormulario.cleaned_data

            name = informacion['name']
            last_name = informacion['last_name']
            email = informacion['email']
            profession = informacion['profession']

            profe = Profesor(name=name,last_name=last_name,email=email,profession=profession)
            profe.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario = ProfeFormulario()
    return render(request, 'AppCoder/profesores.html',{'miFormulario':miFormulario})

def estudiantes(request):

    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid(): # parentesisssss

            informacion = miFormulario.cleaned_data

            name = informacion['name']
            last_name = informacion['last_name']
            email = informacion['email']

            estudiante = Estudiante(name=name,last_name=last_name,email=email)
            estudiante.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario = EstudianteFormulario()
    return render(request, 'AppCoder/estudiantes.html',{'miFormulario':miFormulario})
    #return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse('vista estudiantes')

def entregables(request):

    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid(): # parentesisssss

            informacion = miFormulario.cleaned_data

            name = informacion['name']
            submission_date = informacion['submission_date']
            submitted = informacion['submitted']

            entregable = Entregable (name=name,submission_date=submission_date,submitted=submitted)
            entregable.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario = EntregableFormulario()
    return render(request, 'AppCoder/entregables.html',{'miFormulario':miFormulario})
    #return render(request, 'AppCoder/entregables.html')
    #return HttpResponse('vista entregables')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse('vista cursos')

def formulario(request):
    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST) # acá llega toda la informacion del html

        print(miFormulario)

        if miFormulario.is_valid():   # si pasó la validación de django

            informacion = miFormulario.cleaned_data # django hace una validación interna; nos da solo los valores

            print(informacion)

            name = informacion['name']
            group = informacion['camada']

            curso = Curso (name=name,camada=group)
            curso.save()

            return render(request, 'AppCoder/inicio.html')
    else: # si no es un método POST
        miFormulario = CursoFormulario() # formulario vacío para construir el html
    
    return render(request, 'AppCoder/formulario.html',{'miFormulario':miFormulario})

#        print(request.POST)
#        course = request.POST['curso']
#        camada = request.POST['camada']
#
#        curso = Curso(name = course,camada = camada)
#        curso.save()
#
#        return render(request,'AppCoder/formulario.html')
#    
#    return render(request, 'AppCoder/formulario.html')

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        #respuesta = f"Estoy buscando la camada número: {request.GET['camada'] }"
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        print(cursos)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos,'camada':camada})
    else:
        respuesta = 'no enviaste datos'

    # no olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)
