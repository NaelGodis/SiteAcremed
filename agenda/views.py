from django.contrib.auth.models import User, Group
from agenda.models import Convidado, Local, Agenda
from django.shortcuts import render
from rest_framework import viewsets, permissions
from agenda.serializers import UserSerializers,  GroupSerializers, ConvidadoSerializers, AgendaSerializers, LocalSerializers


# Create your views here.

class ConvidadoViewSet(viewsets.ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializers
    permission_classes = [permissions.IsAuthenticated]


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializers
    permission_classes = [permissions.IsAuthenticated]

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    serializer_class = LocalSerializers
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]
