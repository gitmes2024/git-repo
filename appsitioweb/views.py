from django.shortcuts import render
#from django.http import HttpResponse



# Create your views here.

#def homepage(request):
   # return HttpResponse("Helo word")

#def conferencia(request):
    #return HttpResponse("sitio de las conferencias del MES") 

def inicio(request):
    return render(request, "sitioweb/inicio.html")

def vconferencia(request):
    return render(request, "sitioweb/vconferencia.html")

def tipoconf(request):
    return render(request, "sitioweb/tipoconf.html")

def departamento(request):
    return render(request, "sitioweb/departamento.html")

def sala(request):
    return render(request, "sitioweb/sala.html")