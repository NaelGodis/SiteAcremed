from django.contrib.auth.models import User, Group
from agenda.models import Convidado, Local, Agenda
from rest_framework import viewsets
from agenda.api.serializers import UserSerializers,  GroupSerializers, ConvidadoSerializers, AgendaSerializers, LocalSerializers


# Create your views here.

class ConvidadoViewSet(viewsets.ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializers
    #permission_classes = [permissions.IsAuthenticated]


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializers
    #permission_classes = [permissions.IsAuthenticated]

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializers
    #permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    #permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        desc = self.request.query_params.get('compromisso')
        queryset  = Agenda.objects.all()
        if desc is not None:
            queryset = queryset.filter(compromisso=desc)
        #usuario = self.request.user.username
        #convidado = Convidado.objects.get(usuario__username=usuario)
        #return Agenda.objects.filter(convidado=convidado)
        return queryset


