#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class CursoFormulario(forms.Form):
    # especificar los campos
    name = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class ProfeFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    profession = forms.CharField(max_length=40)

class EstudianteFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    name = forms.CharField(max_length=40)
    submission_date = forms.DateField()
    submitted = forms.BooleanField()

