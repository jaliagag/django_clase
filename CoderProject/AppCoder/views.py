from django.template import loader 
from django.http import HttpResponse

my_template = loader.get_template('index.html')

def inicio(self):
    name = 'jose'
    last_name = 'aliaga'

    my_list = [2,3,4,5,6,1]

    dictionary = {'nombre':name,'apellido':last_name,'lista':my_list}

    document = my_template.render(dictionary) # ya no necesitamos un contexto

    return HttpResponse(document)

def cursos(self):
    return HttpResponse('vista cursos')

def profesores(self):
    return HttpResponse('vista profesores')

def estudiantes(self):
    return HttpResponse('vista estudiantes')

def entregables(self):
    return HttpResponse('vista entregables')
