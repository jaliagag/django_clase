from django.template import loader 
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *
# LISTVIEW
from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse

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

def leerProfesores(request):
    profesores =  Profesor.objects.all() # trae todos los profesores

    contexto = {"profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get(name=profesor_nombre)
    profesor.delete()

    # vuelvo al menú
    profesores =  Profesor.objects.all() # trae todos los profesores

    contexto = {"profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)


def editarProfesor(request,profesor_nombre):
    # recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(name=profesor_nombre)

    # si es el método POST hago lo mismo que el agregar
    if request.method == 'POST':
        miFormulario = ProfeFormulario(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor.name = informacion['name']
            profesor.last_name = informacion['last_name']
            profesor.email = informacion['email']
            profesor.profession = informacion['profession']

            #profe = Profesor(name=name,last_name=last_name,email=email,profession=profession)
            profesor.save()
            return render(request,'AppCoder/inicio.html')
    else:
        miFormulario = ProfeFormulario(initial={'name':profesor.name,'last_name':profesor.last_name,'email':profesor.email,'profession':profesor.profession})
    return render(request, 'AppCoder/editarProfesor.html',{'miFormulario':miFormulario, 'profesor_nombre':profesor_nombre})

# LISTVIEW

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['name','camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['name','camada']

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"

#### estudiantes

### LIST - READ
class EstudiantesList(ListView):
    model = Estudiante
    template_name = "AppCoder/estudiantes2.html"
### DETAIL - READ A UN OBJETO
class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = "AppCoder/estudianteDetalle.html"
    
#### CREATE - 

class EstudianteCreacion(CreateView):
    model = Estudiante
    #success_url = "/AppCoder"
    success_url = '/AppCoder/estudiante/list/'
    fields = ['name','last_name','email']

### UPDATE

class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes2')
    fields = ['name','last_name','email']
### DELETE

class EstudianteBorrar(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiantes2')





