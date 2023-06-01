from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
# Create your views here.
def saludo(request):
 mensaje ="""
<h1>Bienvenidos al curso</h1>
<h2>Mg. Flor Elizabeth Cerdán León</h2>
<h3>Todo lo puedo en Cristo que me fortalece</h3>
"""
 return HttpResponse(mensaje)