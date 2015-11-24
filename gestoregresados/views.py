from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.core.context_processors import csrf
from gestoregresados.models import Egresado, Postgrado, Experiencia, Red

class FormularioEgresado(ModelForm):
	class Meta:
		model = Egresado
		exclude = ["id"]

class FormularioPostgrado(ModelForm):
    class Meta:
        model = Postgrado
        exclude = ["id"]

class FormularioExperiencia(ModelForm):
    class Meta:
        model = Experiencia
        exclude = ["id"]

class FormularioRed(ModelForm):
    class Meta:
        model = Red
        exclude = ["id"]

def salir(request):
	logout(request)
	return HttpResponseRedirect(reverse("gestoregresados.views.main"))

#@login_required(login_url='/')
def ponred(request, pk):	 
    p = request.POST
    red = Red(identr=Egresado.objects.get(pk=pk))
    fr = FormularioRed(p, instance=red)
    fr.save()
    return HttpResponseRedirect(reverse("gestoregresados.views.main"))

def addredes(request, pk):
	identrada = Egresado.objects.get(pk=int(pk))
	p=dict(egresado=identrada, form=FormularioRed())
	p.update(csrf(request))
	return render_to_response("redes.html", p)	

def ponexperiencia(request, pk):
    p = request.POST
    experiencia = Experiencia(identra=Egresado.objects.get(pk=pk))
    fe = FormularioExperiencia(p, instance=experiencia)
    fe.save()
    return HttpResponseRedirect(reverse("gestoregresados.views.main"))

def addexperiencias(request, pk):
	identrada = Egresado.objects.get(pk=int(pk))
	p=dict(egresado=identrada, form=FormularioExperiencia())
	p.update(csrf(request))
	return render_to_response("experiencias.html", p)	

def ponpostgrado(request, pk):
    p = request.POST
    postgrado = Postgrado(identrad=Egresado.objects.get(pk=pk))
    fp = FormularioPostgrado(p, instance=postgrado)
    fp.save()
    return HttpResponseRedirect(reverse("gestoregresados.views.main"))

def addpostgrados(request, pk):
	identrada = Egresado.objects.get(pk=int(pk))
	p=dict(egresado=identrada, form=FormularioPostgrado())
	p.update(csrf(request))
	return render_to_response("postgrados.html", p)	

def main(request):
	entrada = Egresado.objects.all().order_by("fecha_fin")
	return render_to_response("listado.html",dict(entrada=entrada))

def entrada(request,pk):
	identrada = Egresado.objects.get(pk=int(pk))
	mispostgrados = Postgrado.objects.filter(identrad=identrada)
	misexperiencias = Experiencia.objects.filter(identra=identrada)
	misredes = Red.objects.filter(identr=identrada)
	p=dict(linea=identrada, mispostgrados=mispostgrados, misexperiencias=misexperiencias, misredes=misredes)
	p.update(csrf(request))
	return render_to_response("entrada.html",p)

def add(request):
	p=dict(form=FormularioEgresado(), user=request.user)
	p.update(csrf(request))
	return render_to_response("nuevoegresado.html", p)

def nuevoegresado(request):
	p = request.POST
	egresado = Egresado()
	egresado = FormularioEgresado(p,instance=egresado)
	egresado.save()
	return HttpResponseRedirect(reverse("gestoregresados.views.main"))

def delete(request,pk):
	egresado=Egresado.objects.get(pk=int(pk))
	egresado.delete()
	return HttpResponseRedirect(reverse("gestoregresados.views.main"))

def update(request,pk):	
	idegresado = Egresado.objects.get(pk=int(pk))	
	p=dict(egresado=idegresado, form=FormularioEgresado(),user=request.user)
	p.update(csrf(request))
	return render_to_response("updateegresado.html",p)

def modegresado(request,pk):
	p = request.POST
	egremodificado = Egresado.objects.get(pk=int(pk))	
	
	egremodificado.nombre_egresado = p['nombre_egresado']
	egremodificado.apellido_egresado = p['apellido_egresado']
	egremodificado.estado_egresado = p['estado_egresado']
	egremodificado.dir_egresado = p['dir_egresado']
	egremodificado.tel_egresado = p['tel_egresado']
	egremodificado.id_egresado = p['id_egresado']
	egremodificado.titulo_egresado = p['titulo_egresado']
	egremodificado.email_egresado = p['email_egresado']
	egremodificado.fecha_fin = p['fecha_fin']
	egremodificado.save()
	
	return HttpResponseRedirect(reverse("gestoregresados.views.main"))
# git add . * git commit -u "coment" * git origin master ---- https://gist.github.com/bMinaise/7329874 