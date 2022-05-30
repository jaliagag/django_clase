#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.miplantilla),
    path('cursos/',views.cursos),
    path('profesores/',views.profesores),
    path('estudiantes/',views.estudiantes),
    path('entregables/',views.entregables),
    path('applantilla/',views.miplantilla),
]
