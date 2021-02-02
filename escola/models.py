from django.db import models

"""
# Create your models here.
class Documento(models.Model):
        num_doc = models.CharField(max_length=30)

        def __str__(self):
                return self.num_doc
"""

class Escola(models.Model):
        nome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)
        telefone = models.IntegerField(max_length=11, blank=True, null=True)
        email = models.EmailField(max_length=254, null=True, blank=True, unique=True)
        #doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

        def __str__(self):
                return self.nome + ' ' + self.descricao


"""
class Produto(models.Model):
        descricao = models.CharField(max_length=30)
        preco = models.DecimalField(max_digits=5, decimal_places=2)

        def __str__(self):
                return self.descricao

class Venda(models.Model):
        num_venda = models.CharField(max_length=7)
        valor = models.DecimalField(max_digits=5, decimal_places=2)
        desconto = models.DecimalField(max_digits=5, decimal_places=2)
        impostos = models.DecimalField(max_digits=5, decimal_places=2)
        pessoa = models.ForeignKey(Escola, null=True, blank=True, on_delete=models.PROTECT)
        produtos = models.ManyToManyField(Produto, blank=True)

        def __str__(self):
                return self.num_venda

"""