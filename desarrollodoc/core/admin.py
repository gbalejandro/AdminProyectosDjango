from django.contrib import admin

from .models import Proyecto, Desarrollo

#admin.site.register(Proyecto)
#admin.site.register(Desarrollo)

# @admin.register(Proyecto)
# class ProyectoAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'creado', 'creado_por')


# @admin.register(Desarrollo)
# class DesarrolloAdmin(admin.ModelAdmin):
#     list_filter = ('estatus', 'creado')
    #fields = ['version', 'estatus', ('creado', 'actualizado')]
