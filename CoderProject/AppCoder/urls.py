#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from AppCoder import views
#from AppCoder.views import profesores, cursos, estudiantes, formulario, entregables

urlpatterns = [
    path('', views.miplantilla, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'), # los llamamos desde el html
    path('profesores/', views.profesores, name='Profesores'), # es mejor, más controlable
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('formulario/', views.formulario, name='Formulario'),
    path('leerProfesores/', views.leerProfesores, name='LeerProfesores'),
    path('eliminarProfesor/<profesor_nombre>', views.eliminarProfesor, name='EliminarProfesor'),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor, name='EditarProfesor'),
    path('entregables/', views.entregables), # <<<<legacy, no usar!
]
