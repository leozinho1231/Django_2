from django.contrib import admin
from .models import *

class detFilmes(admin.ModelAdmin):
    list_display = ('id','nome','categoriaid')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10



class detCategoria(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10


class detAssinaturas(admin.ModelAdmin):
    list_display = ('id','nome','valor')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10


class detUsuario(admin.ModelAdmin):
    list_display = ('id','nome', 'valor', 'AssinaturaFK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

class detFavoritos(admin.ModelAdmin):
    list_display = ('Filmeid','Usuarioid')
    list_display_links = ('Filmeid',)
    search_fields = ('Usuarioid',)
    list_per_page = 10
    
    
admin.site.register(Filmes, detFilmes)
admin.site.register(Categoria, detCategoria)
admin.site.register(Assinaturas, detAssinaturas)
admin.site.register(Usuario, detUsuario)
admin.site.register(Favoritos, detFavoritos)