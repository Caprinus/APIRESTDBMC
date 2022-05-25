from django.contrib import admin
from .models import Casa, Condominio, Espacios_comunes, Usuario, Seguridad

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Casa)
admin.site.register(Condominio)
admin.site.register(Espacios_comunes)