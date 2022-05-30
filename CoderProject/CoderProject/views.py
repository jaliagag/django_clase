#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template import loader 
from django.http import HttpResponse
from datetime import datetime

def using_loader(self):
    name = 'jose'
    last_name = 'aliaga'
    dt = datetime.now()

    my_list = [2,3,4,5,6,1]

    dictionary = {'nombre':name,'apellido':last_name,'hoy':dt,'lista':my_list}

    my_template = loader.get_template('index.html')

    document = my_template.render(dictionary) # ya no necesitamos un contexto

    return HttpResponse(document)
