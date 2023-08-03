from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#Só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
