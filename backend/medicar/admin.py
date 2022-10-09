from django.contrib import admin
from medicar.models import Especialidade, Medico, Horario, Agenda, Consulta
from django.contrib.auth.models import User

class Users(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')

class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')

class Horarios(admin.ModelAdmin):
    list_display = ('id', 'horario')
    list_display_links = ('id', 'horario')
    search_fields = ('id', 'horario')

class Agendas(admin.ModelAdmin):
    list_display = ('id', 'dia')
    list_display_links = ('id', 'dia')
    search_fields = ('id', 'dia')

admin.site.register(Medico, Medicos)
admin.site.register(Especialidade, Especialidades)
admin.site.register(Horario, Horarios)
admin.site.register(Agenda, Agendas)
