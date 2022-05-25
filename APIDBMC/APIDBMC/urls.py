"""APIDBMC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from apimcdb.models import Casa, Condominio, Espacios_comunes, Usuario, Seguridad
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['url','rut','nombres','apellido1','apellido2','correo','telefono','casa','condominio', 'directiva','conserje','horario','fecha_ingreso', 'habilitado']

class CasaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Casa
        fields = ['url','id_condominio','descripcion','saldo','luz','agua']

class CondominioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condominio
        fields = ['url','nombre_condominio','num_casas','num_casas_ocupadas','mantencion']

class EspaciocomunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Espacios_comunes
        fields = ['url','id_condominio','tipo_espacio','costo_arriendo ','mantencion','aforo','ocupado']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CasaViewSet(viewsets.ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer

class EspaciocomunViewSet(viewsets.ModelViewSet):
    queryset = Espacios_comunes.objects.all()
    serializer_class = EspaciocomunSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'casas', CasaViewSet)
router.register(r'condominios', CondominioViewSet)
router.register(r'espacios_comunes', EspaciocomunViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
