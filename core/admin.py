from django.contrib import admin
from .models import Cliente, Contrato, Planes

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'dni', 'telefono']
    search_fields = ['nombre', 'email', 'dni', 'telefono']

class ContratoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'plan', 'ip', 'fecha_creacion']
    search_fields = ['cliente', 'plan', 'ip']
    list_filter = ['plan', 'fecha_creacion']

class PlanesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'vel_subida', 'vel_bajada', 'precio']
    search_fields = ['nombre', 'vel_subida', 'vel_bajada', 'precio']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Planes, PlanesAdmin)
