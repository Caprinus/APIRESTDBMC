from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Casa, Condominio, Espacios_comunes, Usuario, Seguridad
import json
from django.http import JsonResponse
# Create your views here.


# GPPD para Usuarios
class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def get(self, request, email=''):
        
        if (email !=''):
           usuarios = list(Usuario.objects.filter(correo=email).values())
           if len(usuarios) > 0:   
               usuario=usuarios[0]
               datos = {'usuario': usuario}
           else:
               datos = {'message': "Usuarios not found..."}
           return JsonResponse(datos)
        else:
           usuarios = list(Usuario.objects.values())
           if len(usuarios) > 0:
               datos = {'message': "Success", 'usuarios': usuarios}
           else:
               datos = {'message': "Usuarios not found..."}
           return JsonResponse(datos)
          

    @method_decorator(csrf_exempt)
    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Usuario.objects.create(rut=jd['rut'],nombres=jd['nombres'], apellido1=jd['apellido1'], apellido2=jd['apellido2'], correo=jd['correo'], telefono=jd['telefono'],casa=jd['casa'],  condominio=jd['condominio'], directiva=jd['directiva'],conserje=jd['conserje'],horario=['horario'],fecha_ingreso=['fecha_ingreso'], habilitado=jd['habilitado'])                                                                                                                                         
        datos = {'message': "Success"}
        return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def put(self, request, email):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(correo=email).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id=id)
            usuario.nombres = jd['nombres']
            usuario.correo = jd['correo']
            usuario.habilitado = jd['habilitado']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario not found..."}
        return JsonResponse(datos)

    @method_decorator(csrf_exempt)
    def delete(self, request, email):
        usuarios = list(Usuario.objects.filter(correo=email).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(correo=email).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario not found..."}
        return JsonResponse(datos)

