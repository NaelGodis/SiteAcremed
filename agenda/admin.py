from django.contrib import admin
from agenda.models import Agenda, Local, Convidado

class ConvidadosInLine(admin.TabularInline):
    model = Agenda.convidados.through


class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [
        ConvidadosInLine,
    ]


class AgendaAdmin(admin.ModelAdmin):
    inlines = [
        ConvidadosInLine
    ]
    exclude = ['convidados']

admin.site.register(Agenda,AgendaAdmin)
admin.site.register(Local)
admin.site.register(Convidado,ConvidadoAdmin)
