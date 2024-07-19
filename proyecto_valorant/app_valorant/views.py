from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.

def registro_web(request):
    return render(request,"registro.html")

def registro(request):
    nombre_aux=request.POST["nombre"]
    usuario_aux=request.POST["usuario"]
    email_aux=request.POST["correo"]
    pais_aux=request.POST["nacionalidad"]
    edad=request.POST["edad"]
    contrasena_hash = bcrypt.hashpw(request.POST['contrasena'].encode(), bcrypt.gensalt()).decode()
    if len(nombre_aux)>0 and len(usuario_aux)>0 and len(email_aux)>0 and len(pais_aux)>0 and len(edad)>0 and len(contrasena_hash)>0:
        info=User.objects.create(nombre=nombre_aux,usuario=usuario_aux,email=email_aux,pais=pais_aux,edad=edad,contrasena=contrasena_hash)
        messages.info(request,'usuario registrado ingresado con exito')
    else:
        messages.info(request,'usario no se ha ingresado con exito')
    return HttpResponseRedirect("/registro_web/")


def login(request):
    if request.method == 'GET':
        return redirect("/")
    else:
        if request.method == 'POST':
            
            user = User.objects.filter(usuario=request.POST['usuario']) #Buscamos el correo ingresado en la BD             
            
            if user : #Si el usuario existe

                usuario_registrado = user[0]
                
                if bcrypt.checkpw(request.POST['contrasena'].encode(), usuario_registrado.contrasena.encode()): 
                    usuario = {
                        'id':usuario_registrado.id,
                        'nombre':usuario_registrado.nombre,
                        'usuario':usuario_registrado.usuario,
                        'email':usuario_registrado.email,
                        'pais':usuario_registrado.pais,
                        'edad':usuario_registrado.edad,
                    }
                    mensaje="ingreso correcto"
                    request.session['usuario'] = usuario
                    return HttpResponse(mensaje)
                else:
                    mensaje="ingreso incorrecto"
                    return HttpResponse(mensaje)
            else:
                    mensaje="datos incorrecto"
                    return HttpResponse(mensaje)

def login_web(request):
    return render(request,"login.html")

def contacto(request):
    asunto=request.POST["asunto"]
    correo=request.POST["correo"]
    mensaje=request.POST["mensaje"]
    if len(asunto)>0 and len(correo)>0 and len(mensaje)>0 :
        info=Contacto.objects.create(asunto=asunto,correo=correo,mensaje=mensaje)
        mensaje="mensaje enviado correctamente"
    else:
        mensaje="No se pudo enviar el mensaje"
    return HttpResponse(mensaje)

def contacto_web(request):
    return render(request,"contacto.html")

def jugadas(request):
    idusuario=request.POST["idusuario"]
    mapa=request.POST["mapa"]
    eliminaciones=request.POST["aliminaciones"]
    muertes=request.POST["muertes"]
    agente=request.POST["agente"]
    rango=request.POST["rango"]
    if len(idusuario)>0 and len(mapa)>0 and len(eliminaciones)>0 and len(muertes)>0 and len(agente)>0 and len(rango)>0:
        info=mapas.objects.create(idusuario=idusuario,mapa=mapa,aliminaciones=eliminaciones,muertes=muertes,agente=agente,rango=rango)
        messages.info(request,'jugada ingresado con exito')
    else:
        messages.info(request,'jugada no se ha ingresado con exito')
    return HttpResponseRedirect("/listar_jugadas/")

def jugadas_web(request):
    return render(request,"jugadas.html")


def listar_jugadas_web(request):
    return render(request,"listar_jugadas.html")

def listar_jugadas(request):
    datos = mapas.objects.all()
    return render(request,"listar_jugadas.html",{'informacion':datos})

def base(request):
    return render(request,"base.html")

def index_web(request):
    return render(request,"index.html")

def agentes_web(request):
    return render(request,"agentes.html")

def armas_web(request):
    return render(request,"armas.html")

def entrar_jugadas(request):
    return render(request,"entrarjugadas.html")

def nosotros_web(request):
    return render(request,"nosotros.html")

def mapas_web(request):
    return render(request,"mapas.html")

def radiant_points(request):
    return render(request, 'radiant_points.html')

def carrito(request):
    return render(request, 'carrito.html')