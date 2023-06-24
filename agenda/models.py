from django.db import models

# Create your models here.
class Local(models.Model):
    nome = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.nome} na rua {self.rua} número {self.numero}'

    class Meta:
        verbose_name_plural = "Locais"


class Convidado(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}  - {self.email}'


class Agenda(models.Model):
    compromisso = models.CharField(max_length=255)
    data_inicio = models.DateTimeField(null=True)
    data_fim = models.DateTimeField(null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    convidados = models.ManyToManyField(Convidado)

    def __str__(self):
        return f'{self.compromisso} começa {self.data_inicio} e termina as {self.data_fim}'












