from django.contrib import admin
from medicar.models import Especialidade, Medico, Horario, Agenda, Consulta


class Especialidades(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('id', 'nome')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    exclude = ('deleted_at',)


class Medicos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'get_especialidade')
    list_display_links = ('id', 'nome', 'get_especialidade')
    search_fields = ('id', 'nome')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    exclude = ('deleted_at',)

    @admin.display(ordering='especialidade__nome', description='Especialidade')
    def get_especialidade(self, obj):
        return obj.especialidade.nome


class Horarios(admin.ModelAdmin):
    list_display = ('id', 'horario')
    list_display_links = ('id', 'horario')
    search_fields = ('id', 'horario')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    exclude = ('deleted_at',)


class Agendas(admin.ModelAdmin):
    list_display = ('id', 'dia', 'get_medico')
    list_display_links = ('id', 'dia', 'get_medico')
    search_fields = ('id', 'dia')
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
    exclude = ('deleted_at',)

    @admin.display(ordering='medico__nome', description='Medico')
    def get_medico(self, obj):
        return obj.medico.nome


class Consultas(admin.ModelAdmin):
    list_display = ('id', 'get_medico', 'get_paciente', 'get_horario')
    list_display_links = ('id', 'get_medico', 'get_paciente', 'get_horario')
    search_fields = ('id', 'get_medico', 'get_paciente', 'get_horario')
    readonly_fields = ('created_at', 'updated_at')
    exclude = ('deleted_at',)

    @admin.display(ordering='agenda__medico__nome', description='Medico')
    def get_medico(self, obj):
        return obj.agenda.medico.nome

    @admin.display(ordering='user__name', description='Paciente')
    def get_paciente(self, obj):
        return obj.paciente.email

    @admin.display(ordering='horario__horario', description='Horario')
    def get_horario(self, obj):
        return obj.horario.horario


admin.site.register(Medico, Medicos)
admin.site.register(Especialidade, Especialidades)
admin.site.register(Horario, Horarios)
admin.site.register(Agenda, Agendas)
admin.site.register(Consulta, Consultas)
