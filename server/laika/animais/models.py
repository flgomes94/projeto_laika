from django.db import models

# Create your models here.

class Animal(models.Model):
    sexo = (('1', 'Fêmea'), ('2', 'Macho'), ('3', 'Não sei'))

    nome = models.CharField()
    idade = models.IntegerField()
    sexo = models.CharField()
    peso = models.IntegerField()
    vermifugado = models.BooleanField()
    vacinado = models.BooleanField()
    descricao = models.CharField()
    criador = models.ForeignKey('auth.user', related_name='animais', on_delete=models.CASCADE)

    def save(self, *args,**kwargs):
        super(Animal,self).save(*args, **kwargs)

class Cao(Animal):
    porte_escolhas = (('1', 'Pequeno'), ('2', 'Médio'), ('3', 'Grande'), ('4', 'Extra Grande'))
    porte = models.CharField(max_length=1, choices=size_choices, default='Não sei')

class Gato(Animal):
    # Nothing here yet