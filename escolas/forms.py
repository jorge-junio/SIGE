from django.forms import ModelForm
from .models import Escola, Turma, Aluno, Professor, Disciplina, Habilidade, Matricula, Promove, Contem, Ministra

class EscolaForm(ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'descricao', 'telefone', 'email']


class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'codigoEscola', 'ano']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'descricao', 'telefone', 'email']

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'sobrenome', 'descricao', 'telefone', 'email']

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao',]

class HabilidadeForm(ModelForm):
    class Meta:
        model = Habilidade
        fields = ['nome', 'descricao', 'recompensa']

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['codigoAluno', 'codigoTurma']

class ContemForm(ModelForm):
    class Meta:
        model = Contem
        fields = ['codigoTurma', 'codigoDisciplina']

class PromoveForm(ModelForm):
    class Meta:
        model = Promove
        fields = ['codigoDisciplina', 'codigoHabilidade']

class MinistraForm(ModelForm):
    class Meta:
        model = Ministra
        fields = ['codigoDisciplina', 'codigoProfessor']