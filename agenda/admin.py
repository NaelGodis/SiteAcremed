from django.contrib import admin
from agenda.models import Agenda, Local, Convidado

class AgendaInLine(admin.TabularInline):
    model = Agenda

class ConvidadoAdmin(admin.ModelAdmin):
    inlines = [AgendaInLine]

admin.site.register(Agenda)
admin.site.register(Local)
admin.site.register(Convidado)
