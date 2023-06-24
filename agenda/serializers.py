from django.contrib.auth.models import User,Group
from rest_framework import serializers
from agenda.models import Local, Convidado,Agenda



class LocalSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ['url', 'nome', 'rua','numero']


class ConvidadoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Convidado
        fields = ['url', 'nome', 'email']


class AgendaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ['url', 'compromisso', 'data_inicio', 'data_fim', 'local', 'convidados']



class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']