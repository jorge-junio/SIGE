from django.db import models

class Escola(models.Model):
        nome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)
        telefone = models.IntegerField(blank=True, null=True)
        email = models.EmailField(max_length=254, null=True, blank=True, unique=True)

        def __str__(self):
                return self.nome + ' ' + self.descricao

class Turma(models.Model):
        nome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)
        ano = models.IntegerField(default=2021)
        codigoEscola = models.ForeignKey(Escola, default="" , on_delete=models.PROTECT)

        def __str__(self):
                return self.nome

class Aluno(models.Model):
        nome = models.CharField(max_length=30)
        sobrenome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)
        telefone = models.IntegerField(blank=True, null=True)
        email = models.EmailField(max_length=254, null=True, blank=True, unique=True)

        def __str__(self):
                return self.nome + ' ' + self.sobrenome

class Professor(models.Model):
        nome = models.CharField(max_length=30)
        sobrenome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)
        telefone = models.IntegerField(blank=False, null=True)
        email = models.EmailField(max_length=254, null=True, blank=False, unique=True)

        def __str__(self):
                return self.nome + ' ' + self.sobrenome

class Disciplina(models.Model):
        nome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)

        def __str__(self):
                return self.nome + ' ' + self.descricao

class Habilidade(models.Model):
        nome = models.CharField(max_length=30)
        descricao = models.CharField(max_length=100)
        recompensa = models.CharField(max_length=30)

        def __str__(self):
                return self.nome

class Matricula(models.Model):
        codigoAluno = models.ForeignKey(Aluno, default="", on_delete=models.PROTECT)
        codigoTurma = models.ForeignKey(Turma, default="", on_delete=models.PROTECT)

        def __str__(self):
                return str(self.codigoAluno.nome) + ' - ' + str(self.codigoTurma.nome)

class Contem(models.Model):
        codigoTurma = models.ForeignKey(Turma, default="", on_delete=models.PROTECT)
        codigoDisciplina = models.ForeignKey(Disciplina, null=True, blank=False, default="", on_delete=models.PROTECT)
        
        def __str__(self):
                return str(self.codigoTurma.nome) + ' - ' + str(self.codigoDisciplina.nome)

class Promove(models.Model):
        codigoDisciplina = models.ForeignKey(Disciplina, default="", on_delete=models.PROTECT)
        codigoHabilidade = models.ForeignKey(Habilidade, default="", on_delete=models.PROTECT)
        
        def __str__(self):
                return str(self.codigoDisciplina.nome) + ' - ' + str(self.codigoHabilidade.nome)

class Ministra(models.Model):
        codigoDisciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
        codigoProfessor = models.ForeignKey(Professor, on_delete=models.PROTECT)
        
        def __str__(self):
                return str(self.codigoDisciplina.nome) + ' - ' + str(self.codigoProfessor.nome) + ' ' + str(self.codigoProfessor.sobrenome)