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
    #LISTVIEW
    # CURSOS
    path('curso/list',views.CursoList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(),name='Delete'),
    # ESTUDIANTES
    path('estudiante/list/',views.EstudiantesList.as_view(),name='estudiante_list'),
    path('estudiante/<pk>',views.EstudianteDetalle.as_view(),name='estudiante_detalle'),
    path('estudiante/nuevo/',views.EstudianteCreacion.as_view(),name='estudiante_crear'),
    path('estudiante/edicion/<pk>',views.EstudianteEdicion.as_view(),name='estudiante_editar'),
    path('estudiantes/borrar/<pk>',views.EstudianteBorrar.as_view(),name='estudiante_borrar'),
]

